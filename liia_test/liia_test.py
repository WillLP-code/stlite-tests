import streamlit as st
import pandas as pd
import liiatools

uploaded_file = st.file_uploader('Upload file here:', accept_multiple_files=False)
if uploaded_file:
    try: 
        loaded_file = {uploaded_file.name: pd.read_excel(uploaded_file)}
    except:
        loaded_file = {uploaded_file.name: pd.read_csv(uploaded_file)}
    df = loaded_file

    st.write(loaded_file.name)