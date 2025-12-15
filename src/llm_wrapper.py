"""
Thin wrapper to call an LLM.
Supports:
 - google.generativeai (Gemini)

Loads API keys from Streamlit secrets (cloud) or environment variables (local).
"""

import os
from typing import Optional

# --- Try Streamlit secrets first ---
GENAI_KEY: Optional[str] = None
try:
    import streamlit as st
    GENAI_KEY = st.secrets.get("GOOGLE_API_KEY")
    if GENAI_KEY:
        print(f"[DEBUG] Loaded GOOGLE_API_KEY from Streamlit secrets (ending in ...{GENAI_KEY[-4:]})")
except Exception as e:
    print(f"[DEBUG] Could not load from Streamlit secrets: {e}")

# --- Fallback to environment variables (.env locally) ---
if not GENAI_KEY:
    print("[DEBUG] Key not in secrets, trying environment variables...")
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass
    GENAI_KEY = os.getenv("GOOGLE_API_KEY")
    if GENAI_KEY:
        print(f"[DEBUG] Loaded GOOGLE_API_KEY from environment variables (ending in ...{GENAI_KEY[-4:]})")
    else:
        print("[DEBUG] GOOGLE_API_KEY not found in environment variables.")


# --- Import Gemini ---
GENAI_AVAILABLE = False
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except Exception:
    GENAI_AVAILABLE = False


# --- Configure Gemini ---
if GENAI_AVAILABLE and GENAI_KEY:
    try:
        genai.configure(api_key=GENAI_KEY)
    except Exception as e:
        GENAI_AVAILABLE = False
        print(f"[Gemini] Configuration error: {e}")


# --- Model ---
MODEL_NAME = "gemini-2.5-flash"


SAFETY_PREFIX = (
    "You are a medical assistant. Provide general information only. "
    "Do not give definitive diagnoses. Encourage clinical evaluation. "
)


def generate_with_llm(prompt: str, max_tokens: int = 500) -> str:
    """
    Call Gemini with safety prefix.
    """
    if not GENAI_AVAILABLE:
        raise RuntimeError("Gemini SDK not available.")

    if not GENAI_KEY:
        raise RuntimeError(
            "GOOGLE_API_KEY not found. "
            "Set it in Streamlit Secrets or as an environment variable."
        )

    full_prompt = SAFETY_PREFIX + "\n\n" + prompt

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        resp = model.generate_content(full_prompt)

        text = getattr(resp, "text", None)
        if not text:
            text = str(resp)

        return text[:max_tokens]

    except Exception as e:
        raise RuntimeError(f"Gemini error: {e}")
