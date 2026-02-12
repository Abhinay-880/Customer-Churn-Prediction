# 0 -> female || 1 -> male
# 1 => Yes || 0 => No
# scaler is saved as scaler.pkl
# model is saved as model.pkl
# these are the columns used [Age	Gender	Tenure	MonthlyCharges]

import streamlit as st
import pickle
import numpy as np


scaler = pickle.load(open('scaler.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict churn")

age = st.number_input("Age",min_value=18,max_value=100,value=30)
gender = st.selectbox('Gender',("Female","Male"))
tenure = st.number_input("Tenure",min_value=0,max_value=100,value=12)
monthly_charges = st.number_input("Monthly Charges",min_value=0.0,value=50.0)

gender = 1 if gender == "Male" else 0

if st.button("Predict"):
    input_data = np.array([[age,gender,tenure,monthly_charges]])

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    prob = model.predict_proba(scaled_input)[0][1]

    if prediction == 1:
        st.error("Customer is likely to Churn")
        st.write(f"Churn Probability : {prob:.2f}")
        st.progress(int(prob*100))
    else:
        st.success("Customer is not likely to Churn")
        st.write(f"Churn Probability : {prob:.2f}")
        st.balloons()
