# ===========================================
# Heart Disease Prediction - Premium Dark Theme
# ===========================================

import streamlit as st
import pandas as pd
import pickle as pk

# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="❤️ Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# Load Pipeline
# ==============================
model = pk.load(open("heart_pipeline.pkl", "rb"))

# ==============================
# Custom CSS for Dark Web-Like Theme
# ==============================
st.markdown("""
<style>
body {
    background-color: #1e1e2f;  /* Dark background */
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #9b59b6;  /* Purple headers */
    text-align: center;
}
.card {
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    color: #ffffff;
}
.progress-bar {
    background-color: #3498db; /* Blue progress bar */
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Header
# ==============================
st.markdown("<h1>❤️ Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#3498db;'>Predict the likelihood of heart disease with style!</p>", unsafe_allow_html=True)
st.write("---")

# ==============================
# Sidebar Inputs
# ==============================
st.sidebar.header("👤 Enter Patient Details")

Age = st.sidebar.slider("Age", 20, 100, 40)
Sex = st.sidebar.selectbox("Sex", ["M", "F"])
ChestPainType = st.sidebar.selectbox("Chest Pain Type", ["TA","ATA","NAP","ASY"])
RestingBP = st.sidebar.number_input("Resting BP (mmHg)", 80, 250, 120)
Cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", 100, 600, 200)
FastingBS = st.sidebar.selectbox("Fasting BS > 120 mg/dL", [0,1])
RestingECG = st.sidebar.selectbox("Resting ECG", ["Normal","ST","LVH"])
MaxHR = st.sidebar.number_input("Max Heart Rate", 60, 250, 150)
ExerciseAngina = st.sidebar.selectbox("Exercise Angina", ["Y","N"])
Oldpeak = st.sidebar.number_input("Oldpeak (ST depression)", 0.0, 10.0, 1.0, step=0.1)
ST_Slope = st.sidebar.selectbox("ST Slope", ["Up","Flat","Down"])

# ==============================
# Prediction
# ==============================
if st.button("🚀 Predict Heart Disease"):

    input_data = pd.DataFrame([{
        "Age": Age,
        "Sex": Sex,
        "ChestPainType": ChestPainType,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": FastingBS,
        "RestingECG": RestingECG,
        "MaxHR": MaxHR,
        "ExerciseAngina": ExerciseAngina,
        "Oldpeak": Oldpeak,
        "ST_Slope": ST_Slope
    }])

    pred = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0].max()

    # ==============================
    # Display Result Card
    # ==============================
    if pred == 1:
        st.markdown(f"""
        <div class='card' style='background: linear-gradient(to right, #9b59b6, #2c3e50);'>
        <h2>📉 Prediction: Heart Disease</h2>
        <h3>Confidence: {round(proba*100,2)}%</h3>
        </div>
        """, unsafe_allow_html=True)
        st.progress(int(proba*100))
        if proba > 0.75:
            st.error("⚠️ High Risk! Consult a doctor immediately.")
        elif proba > 0.5:
            st.warning("⚠️ Moderate Risk. Consider lifestyle changes.")
        else:
            st.info("Low Risk, but stay healthy!")
    else:
        st.markdown(f"""
        <div class='card' style='background: linear-gradient(to right, #3498db, #2c3e50);'>
        <h2>🎉 Prediction: No Heart Disease</h2>
        <h3>Confidence: {round(proba*100,2)}%</h3>
        </div>
        """, unsafe_allow_html=True)
        st.progress(int(proba*100))

# ==============================
# Footer
# ==============================
st.write("---")
st.markdown("""
<p style='text-align:center; font-size:14px; color:#9b59b6;'>
Created by <b>Mohamed Ayman</b> | Machine Learning & AI Enthusiast ❤️  
</p>
""", unsafe_allow_html=True)