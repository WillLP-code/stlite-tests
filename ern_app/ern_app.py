import pandas as pd 
import streamlit as st
import json
import plotly.express as px
import numpy as np

def ingress(filepath):
    df['SEX'] = df['SEX'].map({1:'Male',
                        2:'Female'})
    # convert birthday column
    # Get age in years
    # https://stackoverflow.com/questions/31490816/calculate-datetime-difference-in-years-months-etc-in-a-new-pandas-dataframe-c
    # Tip: to convert the age column to whole numbers, rounded down, use: .astype('int') on the column
    df['DOB'] = pd.to_datetime(df['DOB'], format="%d/%m/%Y", errors='coerce')

    df['AGE'] = (pd.to_datetime('today').normalize() - df['DOB'])
    #st.write(type(df['age'][0]))
    # make column for age today
    df['AGE'] = (df['AGE'] / np.timedelta64(1, 'Y')).astype('int')

    return df

def number_of_children(df):
    child_count = len(df['CHILD'].unique())
    return child_count

def boys_girls_count(df):
    counts = df['SEX'].value_counts().to_json()
    counts = json.loads(counts)
    return counts['Male'], counts['Female']

st.title("903 Header analysis tool")

uploaded_files = st.file_uploader('Upload 903 header here:', accept_multiple_files=True)
if uploaded_files:
    loaded_files = {uploaded_file.name[:-4]: pd.read_csv(uploaded_file) for uploaded_file in uploaded_files} 
    
    df = list(loaded_files.values())[0]
    
    df = ingress(df)
    st.dataframe(df)

    child_count = number_of_children(df)
    boys, girls = boys_girls_count(df)

    st.write(f'The number of children is: {child_count}')
    st.write(f'The number of boys is: {boys}')
    st.write(f'The number of girls is: {girls}')

    fig = px.bar(df, x='SEX')
    st.plotly_chart(fig)

    # Make a bar plot for Ethnicity
    fig = px.bar(df, x='ETHNIC')
    st.plotly_chart(fig)

    # Make a histogram plot for age
    # Use google and the plotly docs for this!
    fig = px.histogram(df, x='AGE')
    st.plotly_chart(fig)

