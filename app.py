import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "model.pkl")

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter the transaction amount to predict whether it is Fraud or Legitimate.")

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=0.0,
    step=1.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "amt": [amount]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")