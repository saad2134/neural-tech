from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from hybrid_engine import HybridEngine
from rules_engine import RuleEngine

app = FastAPI(title="Expert System Medical Diagnosis API (Prototype)")

class SymptomsPayload(BaseModel):
    symptoms: Dict[str, bool]
    text: str = ""  # optional user text
    mode: str = "hybrid"  # "rules" | "rag" | "hybrid"

# instantiate shared engine (lazy load rag inside hybrid)
hybrid = HybridEngine()

@app.post("/diagnose")
def diagnose(payload: SymptomsPayload):
    try:
        if payload.mode == "rules":
            engine = RuleEngine()
            matches = engine.evaluate(payload.symptoms)
            return {"mode":"rules","matches":matches}

        elif payload.mode == "rag":
            out = hybrid.rag.query(payload.text or ", ".join([k for k,v in payload.symptoms.items() if v]))
            # return minimal info
            return {"mode":"rag", "retrieved":[{"score":float(s),"text":p["text"]} for s,p in out]}

        elif payload.mode == "hybrid":
            out = hybrid.explain(payload.symptoms, payload.text)
            return {"mode":"hybrid","rule_matches":out["rule_matches"], "retrieved": [{"score":s,"text":p["text"]} for s,p in out["retrieved"]], "llm_summary": out["llm_summary"]}

        else:
            raise HTTPException(status_code=400, detail="Unknown mode")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
