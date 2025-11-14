"""
Thin wrapper to call an LLM.
Supports:
 - google.generativeai (Gemini)

Loads API keys from environment variables (python-dotenv).
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()  # ensure .env is loaded before anything else


# --- Import Gemini ---
GENAI_AVAILABLE = False
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except Exception:
    GENAI_AVAILABLE = False


# --- Load API Key ---
GENAI_KEY = os.getenv("GOOGLE_API_KEY")

if GENAI_AVAILABLE and GENAI_KEY:
    try:
        genai.configure(api_key=GENAI_KEY)
    except Exception as e:
        print(f"[Gemini] Configuration error: {e}")
        GENAI_AVAILABLE = False


# --- Model you requested ---
MODEL_NAME = "gemini-2.5-flash"


SAFETY_PREFIX = (
    "You are a medical assistant. Provide general information only. "
    "Do not give definitive diagnoses. Encourage clinical evaluation. "
)


def generate_with_llm(prompt: str, max_tokens: int = 500) -> str:
    """
    Call Gemini with safety prefix.
    Raises RuntimeError if something is not configured.
    """
    if not (GENAI_AVAILABLE and GENAI_KEY):
        raise RuntimeError("No LLM configured. Set GOOGLE_API_KEY in your .env file.")

    full_prompt = SAFETY_PREFIX + "\n\n" + prompt

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        resp = model.generate_content(full_prompt)

        # Main text output
        text = getattr(resp, "text", None)
        if not text:
            text = str(resp)

        return text[:max_tokens]

    except Exception as e:
        raise RuntimeError(f"Gemini error: {e}")
