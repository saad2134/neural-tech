def medical_diagnosis():
    print("\n============================================")
    print("      SIMPLE MEDICAL DIAGNOSIS SYSTEM")
    print("============================================")
    print("Answer with 'yes' or 'no'. Anything else counts as 'no'.\n")

    # -----------------------------------------
    # 1. COLLECT SYMPTOMS
    # -----------------------------------------
    questions = {
        "fever": "Do you have fever? ",
        "cough": "Do you have cough? ",
        "sore_throat": "Do you have sore throat? ",
        "chills": "Do you have chills? ",
        "sweating": "Do you have sweating? ",
        "headache": "Do you have headache? ",
        "body_pain": "Do you have body pain? ",
        "runny_nose": "Do you have runny nose? ",
        "nausea": "Do you have nausea? ",
        "vomiting": "Do you have vomiting? ",
        "abdominal_pain": "Do you have abdominal pain? ",
        "shortness_breath": "Do you have shortness of breath? ",
        "chest_pain": "Do you have chest pain? ",
        "fatigue": "Do you feel fatigue? ",
    }

    symptoms = {key: (input(text).lower() == "yes") for key, text in questions.items()}

    # -----------------------------------------
    # 2. RULE BASE
    # -----------------------------------------
    rules = [
        {
            "name": "Flu",
            "conditions": ["fever", "cough", "sore_throat"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Classic viral infection triad."
        },
        {
            "name": "Common Cold",
            "conditions": ["runny_nose", "sore_throat", "cough"],
            "severity": "Mild",
            "emergency": False,
            "explanation": "Likely upper respiratory tract infection."
        },
        {
            "name": "Malaria",
            "conditions": ["fever", "chills", "sweating"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "Fever with chills + sweating is typical malarial pattern."
        },
        {
            "name": "Dengue",
            "conditions": ["fever", "headache", "body_pain"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "High fever + severe body ache suggests dengue-like profile."
        },
        {
            "name": "Food Poisoning",
            "conditions": ["nausea", "vomiting", "abdominal_pain"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "GI symptoms indicate food contamination."
        },
        {
            "name": "Heart Attack (Possible)",
            "conditions": ["chest_pain", "shortness_breath", "fatigue"],
            "severity": "Critical",
            "emergency": True,
            "explanation": "Chest pain with breathlessness can signal cardiac emergency."
        },
        {
            "name": "Asthma Attack",
            "conditions": ["shortness_breath", "cough"],
            "severity": "Severe",
            "emergency": True,
            "explanation": "Breathing difficulty with cough suggests airway narrowing."
        }
    ]

    # -----------------------------------------
    # 3. MATCH RULES
    # -----------------------------------------
    matched = []

    for rule in rules:
        if all(symptoms[c] for c in rule["conditions"]):
            matched.append(rule)

    # -----------------------------------------
    # 4. OUTPUT RESULTS
    # -----------------------------------------
    print("\n============================================")

    if not matched:
        print("No clear rule-based diagnosis. Symptoms don’t match known patterns.")
        print("Consider seeking medical consultation.")
        return

    print("Possible Diagnoses:\n")

    for m in matched:
        print(f"🔹 {m['name']}")
        print(f"   • Severity: {m['severity']}")
        print(f"   • Emergency: {'YES' if m['emergency'] else 'No'}")
        print(f"   • Reason: {m['explanation']}\n")

    if any(m["emergency"] for m in matched):
        print("⚠️ WARNING: Some detected conditions require immediate medical attention.\n")

    print("============================================\n")

medical_diagnosis()