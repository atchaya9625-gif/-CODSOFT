import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📩 Spam SMS Detection")

message = st.text_area("Enter SMS Message")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)

        if prediction[0] == "spam":
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")