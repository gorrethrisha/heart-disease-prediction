# Heart Disease Prediction

## Project Overview
This project develops a machine learning-based Heart Disease Prediction system to determine whether a patient has heart disease using various health-related features.

## Objective
The primary objective of this project is to develop a machine learning model to predict the presence of heart disease 

## Dataset Information
- Total Records: **918**
- Total Features: **11**
- Target Variable: **target**
  - `0` → No Heart Disease
  - `1` → Heart Disease

### Features Used in Training
- age
- sex
- chest pain type
- resting bp 
- cholesterol
- fasting blood sugar
- resting ecg
- max heart rate
- exercise angina
- oldpeak
- ST slope

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Methodology

The following steps were followed during the development of the project:

1. Data Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature and Target Separation
4. Train-Test Split
5. Feature Scaling
6. Model Training and Evaluation
   - Logistic Regression
   - Support Vector Classifier (SVC)
   - Random Forest
7. Model Comparison
8. Final Model Selection

## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 88.59% | 87.16% | 93.14% | 90.05% |
| SVC | 88.59% | 85.84% | 95.10% | 90.23% |
| Random Forest | 88.59% | 88.57% | 91.18% | 89.86% |

## Final Model Selection
Logistic Regression, Support Vector Classifier (SVC), and Random Forest models were trained and evaluated for heart disease prediction. Although all three models achieved comparable accuracy, SVC demonstrated the best overall performance by achieving the highest recall and F1-score while effectively minimizing false negative predictions. Therefore, **the Support Vector Classifier (SVC) was selected as the final model for heart disease prediction.**

## Conclusion
A heart disease prediction system was successfully developed and evaluated using multiple classification algorithms. The developed system can assist in the early identification of heart disease and support timely medical intervention.
