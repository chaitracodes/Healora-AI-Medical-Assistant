import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st

st.title("About Healora")

st.write("""
Healora is an AI-powered medical assistant demo designed to provide
general health guidance based on user-reported symptoms.

### Features
- Symptom-based chat guidance
- BMI & calorie calculators
- Voice input support
- PDF report generation

⚠️ Healora does NOT provide medical diagnosis.
Always consult a healthcare professional.

### Tech Stack
- Python
- Streamlit
- SpeechRecognition
- FPDF
""")
