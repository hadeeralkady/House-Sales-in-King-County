import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained pipeline
model_path = r"C:\Users\hadee\Desktop\Data Scientist\Project_Final\model_pipeline.pkl"
model_pipeline = joblib.load(model_path)

# Get all expected features (based on your model's training data)
all_features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront',
    'view', 'condition', 'grade', 'sqft_above', 'sqft_basement',
    'yr_built', 'yr_renovated', 'lat', 'long', 'sqft_living15', 'sqft_lot15', 'date'
]

st.title("🏠 House Price Prediction App")
st.write("Enter available features below. Leave others blank — the model will handle missing data.")

user_input = {}

for feature in all_features:
    if feature == 'date':
        user_input[feature] = st.text_input(f"{feature} (e.g., 20141013T000000)", placeholder='optional') or np.nan
    elif feature in ['lat', 'long']:
        user_input[feature] = st.number_input(f"{feature}", format="%.6f", value=None, placeholder='optional')
    elif feature in ['bathrooms']:
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0, step=0.25, value=None, placeholder='optional')
    else:
        user_input[feature] = st.number_input(f"{feature}", min_value=0, step=1, value=None, placeholder='optional')

# On submit
if st.button('Predict'):
    # Format input into DataFrame
    input_df = pd.DataFrame([{k: (v if v != '' else np.nan) for k, v in user_input.items()}])

    try:
        prediction_log = model_pipeline.predict(input_df)[0]
        prediction_price = np.exp(prediction_log)  # inverse of log(price)
        st.success(f"💰 Estimated House Price: ${prediction_price:,.2f}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")