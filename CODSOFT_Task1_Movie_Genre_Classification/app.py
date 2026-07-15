import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🎬 Movie Genre Classification")

text = st.text_area("Enter Movie Plot")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a movie plot.")
    else:
        data = vectorizer.transform([text])
        prediction = model.predict(data)
        st.success(f"Predicted Genre: {prediction[0]}")