import streamlit as st
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).parent

model = joblib.load(BASE_DIR / "model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")

st.title("📩 Spam SMS Detection")

message = st.text_area("Enter SMS Message")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter an SMS message.")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Ham (Not Spam)")