import streamlit as st
import pickle
import numpy as np


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


st.sidebar.title("📋 Instructions")
st.sidebar.markdown("""
1. Enter your personal and health metrics using the sliders and dropdowns.
2. Click the **'Check Risk'** button to see your heart disease risk.
3. The result will show whether you're at high or low risk.

---
**Tech Stack**:
- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Random Forest Classifier
""")

st.title("💓 Heart Disease Risk Predictor")
st.write("Enter your health details to check your risk level.")
with st.expander("📘 Learn About the Parameters"):
    st.markdown("""
    - **Age**: Age in years. Older age = higher risk.
    - **Sex**: 1 = Male, 0 = Female.
    - **Chest Pain Type (cp)**:
        - 0: Typical Angina  
        - 1: Atypical Angina  
        - 2: Non-Anginal Pain  
        - 3: Asymptomatic
    - **Resting Blood Pressure (trestbps)**: In mm Hg. High = more stress on the heart.
    - **Cholesterol (chol)**: Serum cholesterol in mg/dl.
    - **Fasting Blood Sugar (fbs)**: >120 mg/dl? (1 = Yes, 0 = No)
    - **Resting ECG (restecg)**: 0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy
    - **Max Heart Rate (thalach)**: Higher = better cardio capacity.
    - **Exercise Angina (exang)**: 1 = Yes, 0 = No
    - **ST Depression (oldpeak)**: Depression induced by exercise.
    - **ST Slope (slope)**: 
        - 0: Upsloping  
        - 1: Flat  
        - 2: Downsloping
    """)


age = st.slider("Age", 20, 80, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure", 90, 200, 120)
chol = st.slider("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
thalach = st.slider("Max Heart Rate Achieved", 70, 200, 150)
restecg = st.selectbox("Resting ECG results (0: Normal, 1: ST-T abnormality, 2: probable LVH)", [0, 1, 2])
exang = st.selectbox("Exercise-induced Angina (1 = Yes; 0 = No)", [0, 1])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of peak exercise ST segment", [0, 1, 2])
ca = st.slider("Number of major vessels (0–3) colored by fluoroscopy", 0, 3, 0)
thal = st.selectbox("Thalassemia (1 = normal; 2 = fixed defect; 3 = reversable defect)", [1, 2, 3])


sex_val = 1 if sex == "Male" else 0


input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg, thalach, exang,
                        oldpeak, slope, ca, thal]])


if st.button("Check Risk"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease. Please consult a doctor.")
    else:
        st.success("✅ You are at low risk. Stay healthy!")
