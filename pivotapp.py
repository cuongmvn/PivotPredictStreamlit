import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('HR Helper')

with st.expander("Details"):
    st.write("Welcome to HR Helper")
    st.write("This webapp is meant to make predictions on suitable Machine learning job title.")


uploaded_file = st.file_uploader("Choose a file for prediction")
if uploaded_file is not None:
    res = requests.post(f"https://predictjobtitle.herokuapp.com/predict-csv", uploaded_file)
    st.write(res.json())
