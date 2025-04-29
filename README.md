# House Price Prediction – King County, USA

This project was developed as part of the graduation requirement for the **Digital Egypt Pioneers Initiative – AI & Data Science Track**.

## 📌 Project Objective

To build a predictive machine learning model that accurately estimates house prices based on various features such as location, size, condition, and other attributes using real housing data from King County, USA.

---

## 📊 Dataset

- **Source**: Kaggle – House Sales in King County, USA
- **Size**: 21,613 records with 21 features
- **Target Variable**: `price`

---

## 🧠 Models Applied

- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor (final and best performing model)

---

## 🛠️ Workflow

1. **Exploratory Data Analysis (EDA)**
2. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical features
   - Feature transformation (including log transformation for skewed target)
3. **Model Training & Evaluation**
   - Train-test split and cross-validation
   - Evaluation metrics: R² Score, MAE, MSE
4. **Hyperparameter Tuning**
   - Used `RandomizedSearchCV` on XGBoost for optimal performance
5. **Deployment**
   - Built a simple user interface using **Streamlit** for live predictions

---

## 🧪 Performance Summary

- **Best Model**: XGBoost Regressor
- **R² Score**: 0.86 (on test set after tuning)
- **Features with highest importance**: `grade`, `sqft_living`, `lat`

---

## 🚀 Demo

To run the Streamlit app locally:
```bash
streamlit run app.py
