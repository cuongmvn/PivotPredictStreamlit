import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("HR Helper")

with st.expander("Details"):
    st.write("Welcome to HR Helper")
    st.write("This webapp is meant to make predictions on suitable Machine learning job title.")


st.header("Predict section")
uploaded_predictions_file = st.file_uploader("Choose a file for predictions")
if uploaded_predictions_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_predictions_file, sep=';', decimal = ',')
    df.drop(columns=["Metier"], inplace=True)
    with st.expander("Data details:"):
        st.write(df) 
    res = requests.post(f"https://predictjobtitle.herokuapp.com/predictions", json = {'content': df.to_json()})
    st.write(res.json())

st.sidebar.header("Specify Input Parameters")
def user_input_features():
    Entreprise = st.text_input('Entreprise', 'Sanofi')
    Technologies = st.text_input('Skills', 'Python/Tensorflow/scikit-learn/Deep learning/R')
    
    Diplome = st.sidebar.selectbox(
    "Select your diplome",
    ("Phd", "Master", "Bachelor", "No diploma")
    )
    Experience = st.sidebar.slider('Experience', min_value=0, max_value=20)
    
    Ville = st.multiselect('Work location',
    ['Paris', 'Marseille', 'Nantes', 'Bordeaux', 'Lille', 'Toulouse',
    'Rouen', 'Lyon', 'Strasbourg', 'Grenoble', 'Nice', 'Toulon',
    'Montpellier', 'Rennes'])
    data = {'Entreprise': Entreprise,
            'Technologies': Technologies,
            'Diplome': Diplome,
            'Experience': Experience,
            'Ville': Ville}
    features = pd.DataFrame(data, index=[0])
    return features
    
df = user_input_features()

st.header('Specified Input parameters')
st.write(df)
st.write('---')