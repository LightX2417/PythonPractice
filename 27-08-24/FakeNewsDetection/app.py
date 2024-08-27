import streamlit as st
import joblib

# Load the model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Fake News Detection")

input_text = st.text_area("Enter the news article text:")

if st.button("Predict"):
    if input_text:
        # Transform the input text using the loaded vectorizer
        input_tfidf = vectorizer.transform([input_text])

        # Make a prediction using the loaded model
        prediction = model.predict(input_tfidf)

        # Display the result
        if prediction[0] == 1:
            st.success("This news article is REAL!")
        else:
            st.error("This news article is FAKE!")
    else:
        st.warning("Please enter some text to analyze.")

