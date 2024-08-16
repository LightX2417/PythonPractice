import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("house_price_model.pkl")


# Define function to predict popularity
def predict_popularity(data):
    return model.predict(pd.DataFrame([data]))


# Streamlit app layout
st.title("Song Popularity Predictor")

# Input fields for the parameters
st.sidebar.header("Input Parameters")


def get_input():
    duration_ms = st.sidebar.number_input("Duration (ms)", min_value=0)
    danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.5)
    energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.5)
    loudness = st.sidebar.slider("Loudness (dB)", -60.0, 0.0, -10.0)
    speechiness = st.sidebar.slider("Speechiness", 0.0, 1.0, 0.1)
    acousticness = st.sidebar.slider("Acousticness", 0.0, 1.0, 0.1)
    instrumentalness = st.sidebar.slider("Instrumentalness", 0.0, 1.0, 0.0)
    liveness = st.sidebar.slider("Liveness", 0.0, 1.0, 0.1)
    valence = st.sidebar.slider("Valence", 0.0, 1.0, 0.5)
    tempo = st.sidebar.slider("Tempo (BPM)", 50, 200, 120)
    time_signature = st.sidebar.slider("Time Signature", 3, 7, 4)

    explicit = st.sidebar.selectbox("Explicit", ["True", "False"])
    mode = st.sidebar.selectbox("Mode (Major = 1, Minor = 0)", [1, 0])
    key = st.sidebar.selectbox("Key (0 = C, 1 = C# / Db, ...)", list(range(12)) + [-1])
    track_genre = st.sidebar.text_input("Track Genre")

    return {
        "duration_ms": duration_ms,
        "danceability": danceability,
        "energy": energy,
        "loudness": loudness,
        "speechiness": speechiness,
        "acousticness": acousticness,
        "instrumentalness": instrumentalness,
        "liveness": liveness,
        "valence": valence,
        "tempo": tempo,
        "time_signature": time_signature,
        "explicit": explicit == "True",
        "mode": mode,
        "key": key,
        "track_genre": track_genre,
    }


# Input form
data = get_input()

# Predict button
if st.sidebar.button("Predict"):
    prediction = predict_popularity(data)
    st.write("Predicted Popularity:", round(prediction[0], 2))
