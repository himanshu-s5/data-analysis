import streamlit as st
import pandas as pd

def show():
    st.title("Data Analysis")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        
        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset")
        st.dataframe(df)

        st.subheader("Basic Statistics")
        st.write(df.describe())
        
        st.subheader("Columns")
        st.write(df.columns.tolist())
    else:
        st.write("Please upload a CSV file to analyze.")
