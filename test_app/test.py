import streamlit as st
import pandas as pd

st.title("A test of STlite for D2I")

uploaded_files = st.file_uploader('Choose a file', accept_multiple_files=True)


for uploaded_file in uploaded_files:
    st.write('filename:', uploaded_file.name)
    df = pd.read_csv(uploaded_file)

if uploaded_files:
    st.dataframe(df)