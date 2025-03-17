import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Custom CSS for Improved Design
st.markdown("""
    <style>
    body {background-color: #F0F2F6;}
    .main-title {color: #4CAF50; text-align: center; font-size: 40px; font-weight: bold; text-shadow: 2px 2px #D0D0D0; margin-top: 20px;}
    .subtitle {color: #2196F3; text-align: center; font-size: 28px; font-weight: bold; text-shadow: 1px 1px #D0D0D0;}
    .stButton>button {width: 100%; background-color: #4CAF50; color: white; border-radius: 10px; border: none; padding: 10px;}
    .stButton>button:hover {background-color: #45a049;}
    .input-container {border: 1px solid #ddd; padding: 10px; border-radius: 10px; margin-bottom: 10px; background-color: #ffffff;}
    </style>
    """, unsafe_allow_html=True)

# Load Models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Create Dropdown Menu
selected = st.sidebar.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
)

# Input Display Function
def display_input(label, key):
    return st.number_input(label, key=key, min_value=0.0)

# Prediction Logic
def predict_disease(model, input_data, message):
    try:
        prediction = model.predict([input_data])[0]
        st.success(message if prediction == 1 else f"The person does not have {message.lower()}")
    except Exception as e:
        st.error(f"Error: {str(e)}. Please ensure all inputs are correctly filled.")

# Pages Based on Selection
if selected == 'Diabetes Prediction':
    st.markdown('<h1 class="main-title">Diabetes Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict diabetes:")

    data = [
        display_input('Number of Pregnancies', 'Pregnancies'),
        display_input('Glucose Level', 'Glucose'),
        display_input('Blood Pressure', 'BloodPressure'),
        display_input('Skin Thickness', 'SkinThickness'),
        display_input('Insulin Level', 'Insulin'),
        display_input('BMI', 'BMI'),
        display_input('Diabetes Pedigree Function', 'DPF'),
        display_input('Age', 'Age')
    ]

    if st.button('Predict Diabetes'):
        predict_disease(models['diabetes'], data, 'Diabetes')

elif selected == 'Heart Disease Prediction':
    st.markdown('<h1 class="main-title">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict heart disease:")

    data = [
        display_input('Age', 'age'),
        display_input('Sex (1 = male; 0 = female)', 'sex'),
        display_input('Chest Pain Type (0-3)', 'cp'),
        display_input('Resting Blood Pressure', 'trestbps'),
        display_input('Serum Cholesterol', 'chol'),
        display_input('Fasting Blood Sugar (> 120 mg/dl)', 'fbs'),
        display_input('Resting ECG Results', 'restecg'),
        display_input('Max Heart Rate Achieved', 'thalach'),
        display_input('Exercise Induced Angina (1 = Yes; 0 = No)', 'exang'),
        display_input('Oldpeak', 'oldpeak'),
        display_input('Slope of peak exercise ST segment', 'slope'),
        display_input('Number of major vessels colored by fluoroscopy', 'ca'),
        display_input('Thalassemia (0-3)', 'thal')
    ]

    if st.button('Predict Heart Disease'):
        predict_disease(models['heart_disease'], data, 'Heart Disease')

elif selected == 'Parkinsons Prediction':
    st.markdown('<h1 class="main-title">Parkinson\'s Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict Parkinson's disease:")

    data = [
        display_input(f'{feature}', feature) for feature in [
            'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
            'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
            'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
            'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
        ]
    ]

    if st.button("Predict Parkinson's"):
        predict_disease(models['parkinsons'], data, "Parkinson's Disease")

elif selected == 'Lung Cancer Prediction':
    st.markdown('<h1 class="main-title">Lung Cancer Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict lung cancer:")

    data = [
        display_input(feature, feature) for feature in [
            'Age', 'Gender', 'Smoking', 'Yellow fingers', 'Anxiety',
            'Peer Pressure', 'Chronic Disease', 'Fatigue', 'Allergy',
            'Wheezing', 'Alcohol Consumption', 'Coughing', 'Shortness of Breath',
            'Swallowing Difficulty', 'Chest Pain'
        ]
    ]

    if st.button("Predict Lung Cancer"):
        predict_disease(models['lung_cancer'], data, 'Lung Cancer')

elif selected == 'Hypo-Thyroid Prediction':
    st.markdown('<h1 class="main-title">Hypo-Thyroid Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict hypo-thyroid:")

    data = [
        display_input('Age', 'age'),
        display_input('Sex (1 = Male; 0 = Female)', 'sex'),
        display_input('On Thyroxine (1 = Yes; 0 = No)', 'on_thyroxine'),
        display_input('TSH', 'tsh'),
        display_input('T3', 't3'),
        display_input('TT4', 'tt4'),
        display_input('T4U', 't4u')
    ]

    if st.button('Predict Hypo-Thyroid'):
        predict_disease(models['thyroid'], data, 'Hypo-Thyroid')
