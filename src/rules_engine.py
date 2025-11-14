"""
Rule-based inference engine. Rules can be loaded from JSON or defined inline.
Each rule is a dict with: name, conditions (list), severity, emergency, explanation.
"""

from typing import Dict, List

DEFAULT_RULES = [
    {"name": "Flu", "conditions": ["fever","cough","sore_throat"], "severity":"Moderate", "emergency":False, "explanation":"Viral respiratory infection"},
    {"name": "Common Cold", "conditions": ["runny_nose","sore_throat","cough"], "severity":"Mild", "emergency":False, "explanation":"Upper respiratory infection"},
    {"name": "Malaria", "conditions": ["fever","chills","sweating"], "severity":"Severe", "emergency":False, "explanation":"Parasitic infection — check malaria test"},
    {"name": "Dengue", "conditions": ["fever","headache","body_pain"], "severity":"Severe", "emergency":False, "explanation":"Consider dengue — test platelet counts"},
    {"name": "Heart Attack (Possible)", "conditions":["chest_pain","shortness_breath","fatigue"], "severity":"Critical", "emergency":True, "explanation":"Possible cardiac event — immediate attention"},
    {"name": "Food Poisoning", "conditions":["nausea","vomiting","abdominal_pain"], "severity":"Moderate", "emergency":False, "explanation":"Gastrointestinal infection"}
]

class RuleEngine:
    def __init__(self, rules: List[dict] = None):
        self.rules = rules or DEFAULT_RULES

    def evaluate(self, facts: Dict[str, bool]) -> List[dict]:
        """
        facts: mapping of symptom -> boolean
        """
        matched = []
        for r in self.rules:
            if all(facts.get(cond, False) for cond in r["conditions"]):
                matched.append(r)
        return matched
