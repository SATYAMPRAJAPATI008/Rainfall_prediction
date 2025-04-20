import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("rainfall_prediction_model.pkl")

st.set_page_config(page_title="Rainfall Predictor", layout="centered")
st.title("☔ Rainfall Prediction App")

st.markdown("Enter the weather details below to predict rainfall (in inches):")

# Input fields for weather parameters
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=22.3, step=0.1)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=70.78, step=0.1)
tavg = st.number_input("Average Temperature (TAVG)", value=65.0)
tmax = st.number_input("Maximum Temperature (TMAX)", value=80.0)
tmin = st.number_input("Minimum Temperature (TMIN)", value=50.0)

# Predict button
if st.button("Predict Rainfall"):
    input_df = pd.DataFrame({
        'LATITUDE': [latitude],
        'LONGITUDE': [longitude],
        'TAVG': [tavg],
        'TMAX': [tmax],
        'TMIN': [tmin]
    })
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Rainfall: {prediction:.2f} inches")

st.markdown("---")
st.markdown("Made with ❤ by ChatGPT")
