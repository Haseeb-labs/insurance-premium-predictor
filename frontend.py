import streamlit as st
import requests

# ✅ Correct API URL (local backend)
API_URL = "http://127.0.0.1:8000/predict"

# Page config
st.set_page_config(page_title="Insurance Predictor", page_icon="💡", layout="centered")

# Title
st.title("💡 Insurance Premium Category Predictor")
st.markdown("Enter your details below to predict your insurance premium category.")

# ---------------- INPUT FIELDS ---------------- #

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)

smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")

occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job',
     'business_owner', 'unemployed', 'private_job']
)

# ---------------- BUTTON ---------------- #

if st.button("🚀 Predict Premium Category"):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        # 🔥 API CALL
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        # ✅ SUCCESS CASE
        if response.status_code == 200:
            prediction = result["predicted_category"]

            st.success(f"🎯 Predicted Category: **{prediction}**")

            # Optional: show raw response (for debugging / demo)
            with st.expander("🔍 View Raw API Response"):
                st.json(result)

        # ❌ ERROR CASE
        else:
            st.error(f"❌ API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to FastAPI server. Make sure backend is running.")
