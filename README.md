# Healora – AI Medical Assistant 🩺

Healora is an AI-powered medical assistant web application that provides **general health guidance** based on user-reported symptoms.  
It is designed as a **non-diagnostic**, safety-aware system for educational and demonstration purposes.

---

## ✨ Features

- 💬 Symptom-based health guidance (non-diagnostic)
- 🎤 Voice-based symptom input (local use)
- 📊 BMI and daily calorie calculators
- 📄 Downloadable PDF health chat reports
- 🧭 Multi-page Streamlit interface
- ⚠️ Medical safety disclaimers

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **SpeechRecognition**
- **FPDF**
- **NumPy**

---

## 🧠 How It Works

1. User enters symptoms via text or voice.
2. Rule-based NLP logic detects symptom keywords.
3. The assistant provides structured, safety-aware guidance.
4. Chat history can be exported as a PDF report.
5. Health tools (BMI & calorie calculator) are available via the sidebar.

> ⚠️ Healora does NOT provide medical diagnosis or treatment.

---

## 🚀 Running Locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
