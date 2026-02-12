# Customer Churn Prediction

## 📌 Project Overview
Customer churn prediction is an important business problem where companies aim to identify customers who are likely to stop using their services.  
This project develops a **machine learning classification model** to predict whether a customer will churn based on customer attributes and deploys the model using **Streamlit**.

---

## 🎯 Problem Statement
The objective of this project is to predict whether a customer will churn using the following features:

- Age
- Gender
- Tenure
- Monthly Charges

**Target Variable**
- Churn = 1 → Customer will churn
- Churn = 0 → Customer will not churn

---

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost / Random Forest
- Streamlit
- Pickle

---

## ⚙️ Machine Learning Workflow
1. Data preprocessing and cleaning  
2. Feature encoding and scaling  
3. Model training using classification algorithms  
4. Model evaluation using:
   - Accuracy
   - Precision
   - Recall
   - F1-score  
5. Model serialization using Pickle  
6. Deployment using Streamlit

---

## 📂 Project Structure
customer_churn_project/
    │
    ├── app.py
    ├── Model.pkl
    ├── Scaler.pkl
    ├── requirements.txt
    ├── README.md
    └── notebooks/


---

## ▶️ Running the Application

### Install dependencies

pip install -r requirements.txt

### Run Streamlit app
streamlit run app.py


## 📊 Model Performance

The trained model achieved approximately **80% accuracy on the test dataset**.
Performance evaluation was done using classification metrics such as Precision, Recall, and F1-score.


## 👤 Author

## Abhinay Narmeta