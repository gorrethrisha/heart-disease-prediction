import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("heart_disease_scaler.pkl")

# Title
st.title(" Heart Disease Prediction")
st.write("Enter patient health information to predict heart disease risk.")

# Inputs
age = st.number_input("Age", min_value=28, max_value=77, value=50)

sex = st.selectbox("Sex",["Female", "Male"])

chest_pain_type = st.selectbox("Chest Pain Type",[1, 2, 3, 4])

resting_bp = st.number_input("Resting Blood Pressure",min_value=0,max_value=200,value=120)

cholesterol = st.number_input("Cholesterol",min_value=0,max_value=603,value=200)

fasting_blood_sugar = st.radio("Fasting Blood Sugar",["0", "1"],horizontal=True)

resting_ecg = st.selectbox("Resting ECG",[0, 1, 2])

max_heart_rate = st.number_input("Maximum Heart Rate",min_value=60,max_value=202,value=150)

exercise_angina = st.radio("Exercise Angina",["0", "1"],horizontal=True)

oldpeak = st.number_input("Oldpeak",min_value=-2.6,max_value=6.2,value=0.0)

st_slope = st.selectbox("ST Slope",[0, 1, 2, 3])

# Encoding
sex = 1 if sex == "Male" else 0
fasting_blood_sugar = int(fasting_blood_sugar)
exercise_angina = int(exercise_angina)

# Prediction
if st.button("Predict Heart Disease"):

    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "chest pain type": [chest_pain_type],
        "resting bp s": [resting_bp],
        "cholesterol": [cholesterol],
        "fasting blood sugar": [fasting_blood_sugar],
        "resting ecg": [resting_ecg],
        "max heart rate": [max_heart_rate],
        "exercise angina": [exercise_angina],
        "oldpeak": [oldpeak],
        "ST slope": [st_slope]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")