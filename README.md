# ❤️ Heart Disease Prediction System

---

## 📌 Project Overview
This project builds a **Machine Learning classification system** to predict the likelihood of **Heart Disease** based on patient medical records.  
The system analyzes demographics, vitals, and diagnostic features to identify individuals at risk. Multiple machine learning models were trained and compared to select the most robust one.

---

## 📊 Dataset Description
The dataset contains patient-level medical records:

### 🔹 Demographics & Health Metrics
- **Age**  
- **Sex**  
- **Chest Pain Type**  
- **Resting Blood Pressure (RestingBP)**  
- **Cholesterol**  
- **Fasting Blood Sugar (FastingBS)**  
- **Resting ECG**  
- **Maximum Heart Rate (MaxHR)**  
- **Exercise Induced Angina**  
- **Oldpeak (ST depression)**  
- **ST Slope**

### 🎯 Target Variable
- **HeartDisease** (0 = No, 1 = Yes)

---

## 🤖 Models Implemented
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Decision Tree  
- Random Forest  
- Extra Trees  
- Gradient Boosting  
- Hist Gradient Boosting  
- AdaBoost  
- CatBoost  
- XGBoost  
- Naive Bayes  

---

## 📈 Model Performance Summary

| Model | Train Accuracy | Test Accuracy | Train F1 | Test F1 | Balanced Accuracy |
|-------|----------------|---------------|----------|---------|-----------------|
| CatBoost | 0.9746 | 0.9130 | 0.9771 | 0.9259 | 0.9103 |
| LightGBM | 1.0000 | 0.8913 | 1.0000 | 0.9091 | 0.8840 |
| Random Forest | 1.0000 | 0.8913 | 1.0000 | 0.9074 | 0.8879 |
| Extra Trees | 1.0000 | 0.8804 | 1.0000 | 0.8932 | 0.8865 |
| Gradient Boosting | 0.9407 | 0.8696 | 0.9463 | 0.8909 | 0.8616 |
| Hist Gradient Boosting | 1.0000 | 0.8696 | 1.0000 | 0.8889 | 0.8655 |
| Logistic Regression | 0.8596 | 0.8587 | 0.8731 | 0.8785 | 0.8562 |
| AdaBoost | 0.8753 | 0.8587 | 0.8874 | 0.8785 | 0.8562 |
| Naive Bayes | 0.8596 | 0.8478 | 0.8720 | 0.8704 | 0.8431 |
| SVM | 0.8898 | 0.8370 | 0.9027 | 0.8624 | 0.8299 |
| XGBoost | 1.0000 | 0.8370 | 1.0000 | 0.8571 | 0.8377 |
| KNN | 0.8814 | 0.8152 | 0.8942 | 0.8411 | 0.8114 |
| Decision Tree | 1.0000 | 0.7935 | 1.0000 | 0.8190 | 0.7929 |

✅ **Final Model Selection:**  
- **CatBoost** selected due to its best balance of **accuracy and generalization** (minimal overfitting).

---

## 🛠️ Machine Learning Pipeline
1. Data Cleaning & Preprocessing  
2. Feature Engineering  
3. Encoding Categorical Variables  
4. Train/Test Split  
5. Model Training & Hyperparameter Tuning  
6. Performance Evaluation:
   - Accuracy  
   - Precision  
   - Recall  
   - F1-Score  
   - Balanced Accuracy  
7. Model Comparison & Overfitting Analysis  

---

## 🚀 Healthcare Impact
- Enables early detection of heart disease risk  
- Supports preventive healthcare measures  
- Improves patient monitoring and follow-up planning  
- Reduces unexpected medical emergencies  

---

## 💻 Technologies Used
Python | Pandas | NumPy | Scikit-learn | CatBoost | XGBoost | LightGBM | Matplotlib | Seaborn  

---

## 📌 Conclusion
Ensemble boosting algorithms (CatBoost, AdaBoost, Gradient Boosting) showed superior performance.  
This project highlights the importance of **model comparison, overfitting detection, and balanced evaluation metrics** for building reliable heart disease prediction systems.

---

*Created by **Mohamed Ayman** ❤️ | Machine Learning & AI Enthusiast*
