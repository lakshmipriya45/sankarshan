import streamlit as st
import pandas as pd

dataset=pd.read_csv('data.csv')

st.title('User Driven Review System')

text=st.text_input('Enter the website')

if st.button('Predict'):
  

