Customer Churn Prediction
Project Overview

Customer churn prediction is an important business problem where companies aim to identify customers who are likely to stop using their services.
This project builds a machine learning classification model to predict whether a customer will churn based on customer attributes.

The application also includes a Streamlit web interface where users can input customer details and obtain churn predictions in real time.

Problem Statement

The objective of this project is to predict whether a customer will churn (leave the service) using the following features:

Age

Gender

Tenure

Monthly Charges

Target:

Churn = 1 → Customer will churn

Churn = 0 → Customer will not churn

Technologies Used

Python

Pandas

NumPy

Scikit-learn

XGBoost / Random Forest

Streamlit

Pickle

Machine Learning Workflow

Data preprocessing and cleaning

Feature encoding and scaling

Model training using classification algorithms

Model evaluation using:

Accuracy

Precision

Recall

F1 Score

Model serialization using Pickle

Deployment using Streamlit

Project Structure
customer_churn_project/
│
├── app.py
├── Model.pkl
├── Scaler.pkl
├── requirements.txt
├── README.md
└── notebooks/

Running the Application
Step 1: Install requirements
pip install -r requirements.txt

Step 2: Run Streamlit app
streamlit run app.py

Model Performance

The trained model achieved approximately 80% accuracy on the test dataset.
Evaluation was performed using classification metrics such as Precision, Recall, and F1-score to ensure balanced performance.

Future Improvements

Add more customer behavioral features

Hyperparameter tuning for better performance

Deploy application on cloud platforms

Add churn probability visualization dashboard

Author

Abhinay Narmeta