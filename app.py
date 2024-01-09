import streamlit as st
import pandas as pd
import numpy as np

dataset=pd.read_csv('data.csv')
data=dataset.iloc[:,0].values

st.title('User Driven Review System')

text=st.text_input('Enter the website')

if st.button('Predict'):
  if text in list(data):
    st.success('Original')
  else:
    st.error('Fake')
  

