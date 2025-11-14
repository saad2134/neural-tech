"""
Hybrid engine that:
1. Runs rule-based inference (fast deterministic).
2. Runs RAG to fetch top-k supporting context passages.
3. Calls LLM to produce a human-readable, safe reasoning summary,
   combining facts, matched rules, and retrieved context.
"""

from typing import Dict, Any, List
from rag import RAGIndex
from rules_engine import RuleEngine
from llm_wrapper import generate_with_llm
import pandas as pd
import os

# instantiate components (you can pass prebuilt objects)
rag_index = None

def load_rag_index(index_dir="data/rag_index"):
    global rag_index
    if rag_index is None:
        r = RAGIndex()
        r.load(index_dir)
        rag_index = r
    return rag_index

class HybridEngine:
    def __init__(self, rag: RAGIndex = None, rules: RuleEngine = None):
        self.rag = rag or load_rag_index()
        self.rules = rules or RuleEngine()

    def explain(self, symptoms: Dict[str,bool], user_text: str = "") -> Dict[str, Any]:
        """
        Returns:
         - rule_matches: list
         - retrieved_context: list of passages (text + score)
         - llm_summary: string
        """
        rule_matches = self.rules.evaluate(symptoms)
        # RAG retrieve using either user question or symptom list
        query_text = user_text if user_text else ", ".join([k for k,v in symptoms.items() if v])
        retrieved = self.rag.query(query_text, top_k=5)  # list of (score, passage)
        context_texts = [p["text"] for _, p in retrieved]

        # Build LLM prompt
        prompt = self._build_prompt(symptoms, rule_matches, context_texts, user_text)
        llm_resp = generate_with_llm(prompt)

        return {
            "rule_matches": rule_matches,
            "retrieved": retrieved,
            "llm_summary": llm_resp
        }

    def _build_prompt(self, symptoms, rules, contexts, user_text):
        # Construct a careful, limited prompt
        s_list = [k for k,v in symptoms.items() if v]
        prompt = []
        prompt.append("User symptoms (boolean):")
        prompt.append(str(symptoms))
        prompt.append("\nRule-based matches (if any):")
        prompt.append("\n".join([f"- {r['name']}: {r['explanation']}" for r in rules]) or "None")
        prompt.append("\nRetrieved medical knowledge (short snippets):")
        prompt.extend([f"- {c}" for c in contexts[:5]])
        prompt.append("\nUser text / question:")
        prompt.append(user_text or "N/A")
        prompt.append("\nTask: Using the above, produce a concise, cautious medical reasoning summary with:")
        prompt.append("- Possible conditions (with confidence level: low/moderate/high)")
        prompt.append("- Short justification")
        prompt.append("- Tests to consider")
        prompt.append("- Urgent flags (if any) - be explicit and conservative")
        prompt.append("- A clear disclaimer to seek professional medical care and that this is not definitive.")
        return "\n".join(prompt)
