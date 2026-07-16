import streamlit as st
import joblib
from pathlib import Path

# Get current folder path
BASE_DIR = Path(__file__).parent

# Load model and vectorizer
model = joblib.load(BASE_DIR / "model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")

st.title("🎬 Movie Genre Classification")

text = st.text_area("Enter Movie Plot")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a movie plot.")
    else:
        data = vectorizer.transform([text])
        prediction = model.predict(data)
        st.success(f"Predicted Genre: {prediction[0]}")