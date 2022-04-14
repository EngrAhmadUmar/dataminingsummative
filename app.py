# %%writefile app.py%
import streamlit as st
import pickle
import openpyxl
import xlrd
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


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
    default_value_goes_here = "

    global dataframe
  
    df = pd.read_excel('Test.xlsx')
    dataframe = df
        # st.dataframe(df)
        # st.table(df)

    # attributes = [ball_control, short_passing, dribbling, crossing, curve]
    #
    result = ""
    #
    # # Display Books
    if st.button("Predict"):
      prediction = model.predict(dataframe)

      result = prediction
      st.write(result)


if __name__ == '__main__':
    main()
