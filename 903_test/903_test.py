import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score

uploaded_files = st.file_uploader('Upload 903 data here:', accept_multiple_files=True)
if uploaded_files:
    loaded_files = {uploaded_file.name[:-4]: pd.read_csv(uploaded_file) for uploaded_file in uploaded_files} 
    
    for file in loaded_files.items():
       st.write(file[0])
       st.dataframe(file[1])

