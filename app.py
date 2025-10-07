import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("model/hourly_rate_predictor.pkl")

st.set_page_config(page_title="Freelancer Rate Predictor", layout="wide")

# ----- 🔥 Custom Background Style -----
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2016/09/11/02/45/pc-1660564_1280.jpg"); /* <-- yahan apna image link ya local path lagana */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- Header with right-aligned respected sirs -----
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
        <h1 style='
            color: black;
            -webkit-text-stroke: 1px white;
            font-size: 50px;
            font-weight: bold;
        '>
            💼 Freelancer Hourly Rate Predictor
        </h1>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: right; font-size:18px; font-weight: bold;'>
            Respected Sir Shazaib | Sir Hamza
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <h4 style='
        color: white;
        -webkit-text-stroke: 1px black;
        font-size: 30px;
        font-weight: bold;
    '>
        Fill the form below to estimate the expected hourly rate for a freelancer.
    </h4>
""", unsafe_allow_html=True)




# ----- Input Form -----
with st.form("rate_form"):
    gender = st.selectbox("Gender", ["male", "female", "F", "M", "FEMALE", "MALE"])
    age = st.number_input("Age", min_value=18, max_value=80, step=1)
    country = st.selectbox("Country", ["Pakistan", "India", "Germany", "USA", "Italy", "Australia", "Indonesia"])
    language = st.selectbox("Language", ["English", "German", "Italian", "Indonesian", "Urdu", "Arabic"])
    primary_skill = st.selectbox("Primary Skill", ["Web Development", "Mobile Apps", "Graphic Design", "Blockchain Development", "Data Analysis"])
    years_of_experience = st.slider("Years of Experience", 0, 40)
    rating = st.slider("Freelancer Rating", 0.0, 5.0, step=0.1)
    is_active = st.selectbox("Is Active?", ["Yes", "No"])
    client_satisfaction = st.slider("Client Satisfaction (%)", 0, 100)

    submitted = st.form_submit_button("💰 Predict Hourly Rate")

    # ----- Prediction Logic -----
    if submitted:
        is_active_value = 1 if is_active.lower() in ["yes", "y", "1"] else 0
        input_data = {
            'gender': [gender],
            'age': [age],
            'country': [country],
            'language': [language],
            'primary_skill': [primary_skill],
            'years_of_experience': [years_of_experience],
            'rating': [rating],
            'is_active': [is_active_value],
            'client_satisfaction': [client_satisfaction]
        }
        prediction = model.predict(pd.DataFrame(input_data))[0]
        st.success(f"💲 Estimated Hourly Rate: **${prediction:.2f} USD**")

# ----- Footer -----
st.markdown("""
    <div style='position: fixed; bottom: 10px; left: 10px; font-size:14px; color: gray;'>
        Developed by <strong>Faraz Hussain</strong>
    </div>
""", unsafe_allow_html=True)
