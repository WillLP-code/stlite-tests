import streamlit as st
import pandas as pd
import plotly.express as px



uploaded_file = st.file_uploader('Upload a1 data here:', accept_multiple_files=False)
if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        category = df['category'].unique()
        cat_option = st.selectbox(
        'How would you like to be contacted?',
        (category))
        st.write('You selected:', cat_option)
        df = df[df['category'] == cat_option]
        
        
        category_type = df['category_type'].unique()
        cat_type_option = st.selectbox(
        'How would you like to be contacted?',
        (category_type))
        st.write('You selected:', cat_type_option)
        df = df[df['category_type'] == cat_type_option]
        st.dataframe(df)

        fig = px.line(df, x="time_period", y="number", title=f'{cat_option} : {cat_type_option}')
        st.plotly_chart(fig)

