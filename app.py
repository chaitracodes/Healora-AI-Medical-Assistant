import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
try:
    import speech_recognition as sr
    VOICE_ENABLED = True
except ImportError:
    VOICE_ENABLED = False

from modules.chat_functions import get_ai_response
from modules.pdf_export import export_chat_pdf
from modules.health_tools import calculate_bmi, calculate_calories

# --------------------
# Page Configuration
# --------------------
st.set_page_config(
    page_title="Healora - AI Medical Assistant",
    layout="wide"
)

# --------------------
# Title & Intro
# --------------------
st.markdown("## 👋 Welcome to Healora")
st.write(
    "Describe your symptoms to receive general health guidance. "
    "Use the sidebar to explore health calculators and other pages."
)

st.markdown("## 💊 Healora: AI Medical Assistant")

st.warning(
    "⚠️ **Medical Disclaimer:** Healora provides general health guidance only. "
    "It is **NOT a diagnostic tool** and does not replace professional medical advice."
)

# --------------------
# Session State
# --------------------
if "history" not in st.session_state:
    st.session_state.history = []

# --------------------
# Sidebar: Health Tools
# --------------------
st.sidebar.markdown("## 🧮 Health Tools")

weight = st.sidebar.number_input("Weight (kg)", 40, 200)
height = st.sidebar.number_input("Height (cm)", 100, 250)
age = st.sidebar.number_input("Age", 10, 100)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity = st.sidebar.selectbox(
    "Activity Level",
    ["Sedentary", "Light", "Moderate", "Active"]
)

if st.sidebar.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.sidebar.success(f"Your BMI is: {bmi}")

if st.sidebar.button("Calculate Calories"):
    calories = calculate_calories(age, weight, height, gender, activity)
    st.sidebar.success(f"Your daily calories: {calories} kcal")

# --------------------
# Chat Section
# --------------------
st.markdown("## 💬 Chat with Healora")

# Clear Chat Button (UX Upgrade)
col1, col2 = st.columns([1, 5])
with col1:
    if st.button("🗑️ Clear Chat"):
        st.session_state.history = []
        st.experimental_rerun()

if VOICE_ENABLED:
    use_voice = st.checkbox("🎤 Use Voice Input")
else:
    st.info("🎤 Voice input works only in local setup.")
    use_voice = False

user_input = ""

if use_voice:
    if st.button("Start Recording"):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                st.info("Listening...")
                audio = recognizer.listen(source, timeout=5)

            user_input = recognizer.recognize_google(audio)
            st.success(f"You said: {user_input}")

        except Exception:
            st.error("⚠️ Could not access microphone or recognize speech.")
else:
    user_input = st.text_input("Type your symptoms or question:")

# --------------------
# Process Chat
# --------------------
if user_input:
    st.session_state.history.append(
        {"role": "user", "content": user_input}
    )

    response = get_ai_response(user_input)

    st.session_state.history.append(
        {"role": "bot", "content": response}
    )

# --------------------
# Display Chat (Readable UI)
# --------------------
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(
            f"""
            <div style="
                text-align: right;
                background-color: #DCF8C6;
                color: #000000;
                padding: 10px;
                border-radius: 10px;
                margin: 5px 0;">
                {chat['content']}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="
                text-align: left;
                background-color: #F1F0F0;
                color: #000000;
                padding: 10px;
                border-radius: 10px;
                margin: 5px 0;">
                {chat['content']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --------------------
# Export Chat as PDF
# --------------------
if st.button("📄 Export Chat as PDF"):
    chat_lines = []
    for chat in st.session_state.history:
        role = "You" if chat["role"] == "user" else "Healora"
        chat_lines.append(f"{role}: {chat['content']}")

    filename = export_chat_pdf(chat_lines)
    st.success(f"Chat exported successfully as **{filename}**")
