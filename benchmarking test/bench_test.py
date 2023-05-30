import streamlit as st
import pandas as pd
import plotly.express as px



uploaded_file = st.file_uploader('Upload a1 data here:', accept_multiple_files=False)
if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        category = df['category'].unique()        
        

        with st.sidebar:
            cat_option = st.sidebar.selectbox(
            'What data category would you like?',
            (category))
            st.write('You selected:', cat_option)
        df = df[df['category'] == cat_option]
        
        with st.sidebar:
            category_type = df['category_type'].unique()
            cat_type_option = st.sidebar.selectbox(
            'What sub-category would you like?',
            (category_type))
            st.write('You selected:', cat_type_option)
        df = df[df['category_type'] == cat_type_option]
        st.dataframe(df)

        fig = px.line(df, x="time_period", y="number", title=f'{cat_option} : {cat_type_option}')
        st.plotly_chart(fig)

