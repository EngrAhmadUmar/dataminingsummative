# %%writefile app.py%
import streamlit as st
import pickle
import openpyxl
import xlrd
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from keras.optimizers import adam_v2
from keras.layers import Dropout
from keras import regularizers
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense


# loading the trained model
model = pickle.load(open('Model.pkl','rb'))


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:#002E6D;padding:20px;font-weight:15px"> 
    <h1 style ="color:white;text-align:center;"> Parkinston Disease Prediction</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    default_value_goes_here = ""
    uploaded_file = st.file_uploader("Please upload a XLSX file containing vitals details of the patient(s) you want to predict for.", type="xlsx")

    global dataframe
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        dataframe = df
    result = ""

    if st.button("Predict"):
      prediction = model.predict(dataframe.iloc[: , 1:])

      result = prediction
      st.write(result)


if __name__ == '__main__':
    main()
