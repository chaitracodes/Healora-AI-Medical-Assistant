import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from modules.health_tools import calculate_bmi, calculate_calories

st.title("Health Tools")

st.subheader("BMI Calculator")
w = st.number_input("Weight (kg)", 40, 200)
h = st.number_input("Height (cm)", 100, 250)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(w, h)
    st.success(f"Your BMI is: {bmi}")

st.subheader("Daily Calorie Needs")
age = st.number_input("Age", 10, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Light", "Moderate", "Active"]
)

if st.button("Calculate Calories"):
    calories = calculate_calories(age, w, h, gender, activity)
    st.success(f"Calories needed: {calories} kcal")
