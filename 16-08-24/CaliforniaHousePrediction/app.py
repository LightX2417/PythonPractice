import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title of the app
st.title("House Price Prediction App")

# Sidebar for user input
st.sidebar.header("Input Features")


def user_input_features():
    longitude = st.sidebar.slider(
        "Longitude", min_value=-125.0, max_value=-114.0, value=-121.0
    )
    latitude = st.sidebar.slider("Latitude", min_value=32.0, max_value=42.0, value=37.0)
    housing_median_age = st.sidebar.slider(
        "Housing Median Age", min_value=1, max_value=100, value=30
    )
    total_rooms = st.sidebar.slider(
        "Total Rooms", min_value=1, max_value=10000, value=2000
    )
    total_bedrooms = st.sidebar.slider(
        "Total Bedrooms", min_value=1, max_value=5000, value=300
    )
    population = st.sidebar.slider(
        "Population", min_value=1, max_value=50000, value=1000
    )
    households = st.sidebar.slider("Households", min_value=1, max_value=5000, value=500)
    median_income = st.sidebar.slider(
        "Median Income", min_value=0.0, max_value=15.0, value=5.0
    )

    ocean_proximity = st.sidebar.selectbox(
        "Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    )

    # Convert input data to a dataframe
    data = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity,
    }

    features = pd.DataFrame(data, index=[0])
    return features


# Get user input features
input_df = user_input_features()

# Display user input features for debugging
st.subheader("User Input Features")
st.write(input_df)

# One-hot encode the 'ocean_proximity' feature
input_df = pd.get_dummies(input_df, columns=["ocean_proximity"], drop_first=True)

# Ensure all columns match the training data
required_columns = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
    "ocean_proximity_INLAND",
    "ocean_proximity_ISLAND",
    "ocean_proximity_NEAR BAY",
    "ocean_proximity_NEAR OCEAN",
]

# Add missing columns
for col in required_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match the training data
input_df = input_df[required_columns]

# Scale the input data
input_df_scaled = scaler.transform(input_df)

# Make prediction
prediction = model.predict(input_df_scaled)

# Display prediction
st.subheader("Predicted House Price")
st.write(f"${prediction[0]:,.2f}")
