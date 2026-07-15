import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model.pk1")

st.title("💳 Credit Card Fraud Detection")

amount = st.number_input("Enter Transaction Amount", min_value=0.0)

if st.button("Predict"):
    data = pd.DataFrame([[amount]], columns=["amt"])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Fraud Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")