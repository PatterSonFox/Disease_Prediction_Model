import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Custom CSS for Improved Design
st.markdown("""
    <style>
    body {background-color: #F0F2F6;}
    .main-title {color: #4CAF50; text-align: center; font-size: 36px; margin-top: 20px;}
    .subtitle {color: #2196F3; text-align: center; font-size: 24px;}
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
        display_input('Exercise Induced Angina (1 = Yes; 0 = No)', 'exang')
    ]

    if st.button('Predict Heart Disease'):
        predict_disease(models['heart_disease'], data, 'Heart Disease')

elif selected == 'Parkinsons Prediction':
    st.markdown('<h1 class="main-title">Parkinson\'s Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict Parkinson's disease:")

    data = [
        display_input('MDVP:Fo(Hz)', 'fo'),
        display_input('MDVP:Fhi(Hz)', 'fhi'),
        display_input('MDVP:Flo(Hz)', 'flo'),
        display_input('MDVP:Jitter(%)', 'Jitter_percent'),
        display_input('MDVP:RAP', 'RAP')
    ]

    if st.button("Predict Parkinson's"):
        predict_disease(models['parkinsons'], data, "Parkinson's Disease")

elif selected == 'Lung Cancer Prediction':
    st.markdown('<h1 class="main-title">Lung Cancer Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following details to predict lung cancer:")

    data = [
        display_input('Gender (1 = Male; 0 = Female)', 'GENDER'),
        display_input('Age', 'AGE'),
        display_input('Smoking (1 = Yes; 0 = No)', 'SMOKING'),
        display_input('Yellow Fingers', 'YELLOW_FINGERS'),
        display_input('Anxiety', 'ANXIETY'),
        display_input('Peer Pressure', 'PEER_PRESSURE'),
        display_input('Chronic Disease', 'CHRONIC_DISEASE'),
        display_input('Fatigue', 'FATIGUE'),
        display_input('Allergy', 'ALLERGY'),
        display_input('Wheezing', 'WHEEZING'),
        display_input('Alcohol Consuming', 'ALCOHOL_CONSUMING'),
        display_input('Coughing', 'COUGHING'),
        display_input('Shortness of Breath', 'SHORTNESS_OF_BREATH'),
        display_input('Swallowing Difficulty', 'SWALLOWING_DIFFICULTY'),
        display_input('Chest Pain', 'CHEST_PAIN')
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
        display_input('TSH Level', 'tsh'),
        display_input('T3 Level', 't3'),
        display_input('TT4 Level', 'tt4'),
        display_input('T4U Level', 't4u')
    ]

    if st.button('Predict Hypo-Thyroid'):
        predict_disease(models['thyroid'], data, 'Hypo-Thyroid')
