import streamlit as st
import joblib
import numpy as np


st.header("Medical Insurance Cost Predictor")

model = joblib.load(r"C:\Users\hp\Desktop\14 Days 14 Models\Day 3\model.pkl")
cols = joblib.load(r"C:\Users\hp\Desktop\14 Days 14 Models\Day 3\features.pkl")


# age	gender	bmi	children	smoker	region	occupation	annual_income_usd	exercise_level	chronic_diseases	doctor_visits_per_year	hospitalizations_last_year	alcohol_consumption_per_week	insurance_plan

age = st.number_input("Enter your age:")
gender = st.selectbox("Gender",["Male", "Female"])
bmi = st.number_input("Enter your BMI:")
children = st.number_input("Enter your no of Children:")
smoker = st.selectbox("Smoker",["Yes", "No"])
region = st.selectbox("Region",['Northeast' 'Northwest' 'Central' 'Southeast' 'Southwest'])
occupation = st.selectbox("Occupation",['Driver' 'Doctor' 'Teacher' 'Engineer' 'Nurse' 'Lawyer' 'Office Worker'
 'Construction Worker' 'Technician' 'Manager' 'Retail Worker'])
annual_income_usd = st.number_input("Enter your annual_income_usd:")
exercise_level = st.selectbox("Exercise Level",['Moderate' 'High' 'Low'])
chronic_diseases = st.selectbox("Chronic Diseases",["Yes", "No"])
doctor_visits_per_year = st.number_input("Enter your doctor_visits_per_year:")
hospitalizations_last_year = st.number_input("Enter your hospitalizations_last_year:")
alcohol_consumption_per_week = st.number_input("Enter your alcohol_consumption_per_week:")
insurance_plan = st.selectbox("Insurance Plan",['Basic' 'Standard' 'Premium' 'Gold'])

if chronic_diseases == "Yes":
    chronic_diseases = 1
else: 
    chronic_diseases = 0

feature_input =  np.array([[total_length_cm, body_depth_cm, body_width_cm, head_length_cm, eye_diameter_mm, weight_gr]])
