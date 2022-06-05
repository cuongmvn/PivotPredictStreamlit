import streamlit as st
import pandas as pd
import numpy as np
import requests
z
st.title('HR Helper')

with st.expander("Details"):
    st.write("Welcome to HR Helper")
    st.write("This webapp is meant to make predictions on suitable Machine learning job title.")


st.header('Predict section')
uploaded_predictions_file = st.file_uploader("Choose a file for predictions")
if uploaded_predictions_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_predictions_file)
    with st.expander("Data details:"):
        st.write(dataframe) 
    res = requests.post(f"https://predictjobtitle.herokuapp.com/predictions", json = {'content': dataframe.to_json()})
    st.write(res.json())