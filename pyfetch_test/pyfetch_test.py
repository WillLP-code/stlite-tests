import streamlit as st
import pandas as pd
from pyodide.http import open_url

data = open_url("https://raw.githubusercontent.com/WillLP-code/stlite-tests/main/benchmarking%20test/data/a1.csv")

df = pd.read_csv(data)

st.dataframe(df)