import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("best_rainfall_model.pkl")

# Streamlit app UI
st.set_page_config(page_title="Rainfall Predictor", layout="centered")

st.title("🌧️ Rainfall Prediction App")
st.markdown("Enter the weather data below to predict precipitation (PRCP in inches):")

# Input fields
lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=22.3, format="%.4f")
lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=70.783, format="%.4f")
tavg = st.number_input("Average Temperature (°F)", value=67.0)
tmax = st.number_input("Max Temperature (°F)", value=80.0)
tmin = st.number_input("Min Temperature (°F)", value=52.0)

# Predict button
if st.button("Predict Rainfall"):
    features = np.array([[lat, lon, tavg, tmax, tmin]])
    prediction = model.predict(features)[0]
    st.success(f"🌧️ Predicted Rainfall (PRCP): **{prediction:.2f} inches**")
