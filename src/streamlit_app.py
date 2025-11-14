import streamlit as st
from rules_engine import RuleEngine
from hybrid_engine import HybridEngine, load_rag_index
from llm_wrapper import generate_with_llm
import pandas as pd
import os

st.set_page_config(page_title="Expert System: Medical Diagnosis", layout="centered")

st.title("Expert System — Medical Diagnosis (Prototype)")
st.markdown("**Disclaimer:** Prototype only. This is not medical advice.")

# Sidebar: choose mode
mode = st.sidebar.radio("Choose layer", ["Rule-Based", "RAG (Knowledge)", "Hybrid (Rule+RAG+LLM)"])

# symptom checklist
SYMPTOMS = [
    "fever","cough","sore_throat","chills","sweating","headache","body_pain",
    "runny_nose","nausea","vomiting","abdominal_pain","shortness_breath","chest_pain","fatigue"
]
st.header("Enter symptoms")
cols = st.columns(3)
symptom_flags = {}
for i, s in enumerate(SYMPTOMS):
    with cols[i % 3]:
        symptom_flags[s] = st.checkbox(s.replace("_"," "), key=s)

user_text = st.text_area("Optional: Describe your symptoms in your own words (helps RAG/LLM)", height=100)

# buttons
if st.button("Run"):
    # RULE MODE
    engine = RuleEngine()
    if mode == "Rule-Based":
        matches = engine.evaluate(symptom_flags)
        if not matches:
            st.warning("No rule matched. Consider using Hybrid mode or consult a doctor.")
        else:
            for m in matches:
                st.subheader(m["name"])
                st.write("Severity:", m["severity"])
                st.write("Emergency:", m["emergency"])
                st.write("Why:", m["explanation"])

    elif mode == "RAG (Knowledge)":
        # ensure index loaded
        rag = load_rag_index()
        query = user_text if user_text.strip() else ", ".join([k for k,v in symptom_flags.items() if v])
        results = rag.query(query, top_k=5)
        st.subheader("Retrieved knowledge (top matches)")
        for score, passage in results:
            st.write(f"- (score: {score:.3f}) {passage['text']}")

    elif mode == "Hybrid (Rule+RAG+LLM)":
        st.info("Running hybrid engine (rules + RAG + LLM)...")
        hybrid = HybridEngine()
        out = hybrid.explain(symptom_flags, user_text)
        st.subheader("Rule Matches")
        if not out["rule_matches"]:
            st.write("No rule matches.")
        else:
            for r in out["rule_matches"]:
                st.markdown(f"**{r['name']}** — Severity: {r['severity']} — Emergency: {r['emergency']}")
                st.write(r["explanation"])

        st.subheader("Retrieved Context (top)")
        for score, p in out["retrieved"]:
            st.write(f"- ({score:.3f}) {p['text'][:400]}")

        st.subheader("LLM Summary (cautious)")
        st.write(out["llm_summary"])
