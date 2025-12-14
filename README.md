# 🩺 Neural Tech: Medical Diagnosis

A lightweight hybrid AI framework for modeling, testing, and evaluating medical diagnostic logic.



## 🚀 Overview

This project implements a **Simple Medical Diagnosis Expert System** using three complementary approaches:

1. **Rule-Based (If–Else) Reasoning**
   Deterministic logic using a predefined knowledge base.

2. **Retrieval-Augmented Generation (RAG)**
   Enhances reasoning by retrieving contextual medical knowledge to reduce hallucination and improve accuracy.

3. **LLM-Based (API) Inference**
   Uses large-language-model reasoning to deliver adaptive, context-aware medical insights.

Combined, these layers form a **hybrid expert system** that demonstrates how classical AI and modern generative AI can work together for clinical triage-style decision support.



## 🧠 Concept

An expert system uses:

* **Knowledge Base:** Medical rules and symptom–disease mapping
* **Inference Engine:** Matches user-reported symptoms with predefined rules
* **User Interface:** A simple Streamlit UI for interaction

The system provides probable diagnoses such as **Flu**, **Common Cold**, **Malaria**, **Typhoid**, etc., based on symptom combinations.



## ⚙️ How It Works

### 1. User Input

Users enter symptoms (e.g., `fever`, `cough`, `sore throat`).

### 2. Fact Collection

Symptoms are stored as facts in memory.

### 3. Inference

The engine compares facts with the rule base.

### 4. Diagnosis

Matching rules trigger one or more possible medical conditions.

### 5. Hybrid Layering

| Layer             | Role               | Handles                                    |
| ----------------- | ------------------ | ------------------------------------------ |
| **If–Else Rules (Python If-Else or Prolog)** | Explicit logic     | Known symptom patterns, emergencies        |
| **RAG Retrieval** | Semantic matching  | Variants of symptoms, contextual knowledge |
| **LLM API**       | Adaptive reasoning | Combining logic + retrieved data           |

<img width="1116" height="565" alt="download" src="https://github.com/user-attachments/assets/081906f7-639f-40e3-b23b-035170293208" />



## 📚 Knowledge Base (Example)

| Symptom             | Possible Diseases                  | Severity | Recommended Tests        | Advice                            | Emergency |
| ------------------- | ---------------------------------- | -------- | ------------------------ | --------------------------------- | --------- |
| Fever               | Viral Infection, Malaria, Typhoid  | Moderate | CBC, Malaria Test        | Hydration, paracetamol, rest      | No        |
| Chest Pain          | Heart Attack, Acid Reflux, Anxiety | Severe   | ECG, Troponin            | Seek emergency care if persistent | Yes       |
| Cough               | Cold, Bronchitis, COVID-19         | Mild     | CXR, COVID test          | Steam inhalation, syrup           | No        |
| Shortness of Breath | Asthma, Pneumonia, Heart Failure   | Severe   | X-Ray, Oxygen saturation | Immediate medical care            | Yes       |
| …                   | …                                  | …        | …                        | …                                 | …         |



## 🧩 Components

* **Rule Base:** Hard-coded medical rules
* **Inference Engine:** Pattern matching based on symptoms
* **RAG Pipeline:** Fetches semantically relevant medical context
* **LLM API:** Generates summarized reasoning
* **UI:** Streamlit-based interactive interface



## 🧪 Sample Rule-Based Logic (Simplified)

```python
if fever and cough and sore_throat:
    diagnosis = "Flu"
elif fever and chills and sweating:
    diagnosis = "Malaria"
else:
    diagnosis = "No rule-based match found"
```


## 📌 Features

* ✔ Rule-based medical diagnosis
* ✔ RAG-enhanced symptom interpretation
* ✔ LLM-driven clinical reasoning
* ✔ Emergency detection flags
* ✔ Recommended tests + treatment guidance
* ✔ Modular design for integration with telemedicine tools
* ✔ Easy to extend / plug in new medical rules



## 🎯 Applications

* Educational tools for learning AI reasoning
* Basic medical triage systems
* Hybrid medical-AI prototypes
* Telemedicine support platforms
* Context-aware symptom analysis with live API access



## 📦 Output Example

The system provides:

* Possible diseases
* Severity level
* Recommended tests
* Treatment suggestions
* Emergency status
* RAG-supported context
* LLM summary reasoning

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (Frontend)
* **FAISS / Chroma** (Optional RAG Vector Store)
* **Transformers / Embeddings**
* **LLM API (OpenAI / Gemini / Local LLM)**

## 🖥️ Running the Project

```bash
# Clone the repo
git clone https://github.com/saad2134/expert-system-medical-diagnosis

# Navigate to project
cd expert-system-medical-diagnosis

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run src/streamlit_app.py
```


## 📊 **Repo Stats**

<div align="center">
  
![Repo Size](https://img.shields.io/github/repo-size/saad2134/expert-system-medical-diagnosis)
![Last Commit](https://img.shields.io/github/last-commit/saad2134/expert-system-medical-diagnosis)
![Open Issues](https://img.shields.io/github/issues/saad2134/expert-system-medical-diagnosis)
![Open PRs](https://img.shields.io/github/issues-pr/saad2134/expert-system-medical-diagnosis)
![License](https://img.shields.io/github/license/saad2134/expert-system-medical-diagnosis)
![Forks](https://img.shields.io/github/forks/saad2134/expert-system-medical-diagnosis?style=social)
![Stars](https://img.shields.io/github/stars/saad2134/expert-system-medical-diagnosis?style=social)
![Watchers](https://img.shields.io/github/watchers/saad2134/expert-system-medical-diagnosis?style=social)
![Contributors](https://img.shields.io/github/contributors/saad2134/expert-system-medical-diagnosis)
![Languages](https://img.shields.io/github/languages/count/saad2134/expert-system-medical-diagnosis)
![Top Language](https://img.shields.io/github/languages/top/saad2134/expert-system-medical-diagnosis)

</div>

## ⭐ Star History

<a href="https://www.star-history.com/#saad2134/expert-system-medical-diagnosis&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=saad2134/expert-system-medical-diagnosis&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=saad2134/expert-system-medical-diagnosis&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=saad2134/expert-system-medical-diagnosis&type=Date" />
 </picture>
</a>

---

## ✍️ Endnote
<p align="center">⭐ Star this repo if you found it helpful! Thanks for reading.</p>

---

## 🏷 Tags  

`#ExpertSystem` `#MedicalDiagnosis` `#RuleBasedAI` `#RAG` `#RetrievalAugmentedGeneration` `#HybridAI` `#LLMInference` `#AIinHealthcare` `#HealthTech` `#DiagnosticAI` `#MedicalTriage` `#InferenceEngine` `#KnowledgeBase` `#StreamlitApp` `#AIDecisionSupport` `#SymptomChecker` `#ClinicalDecisionSupport` `#AIHealthcareTools` `#MachineReasoning` `#expert-system-medical-diagnosis` `NeuralTech`

