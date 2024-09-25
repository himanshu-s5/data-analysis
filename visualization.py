import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Data Visualization")

    uploaded_file = st.file_uploader("Choose a CSV file for visualization", type="csv")

    if uploaded_file is not None:
        
        df = pd.read_csv(uploaded_file)

        plot_type = st.selectbox("Choose plot type", ["Scatter Plot", "Line Plot", "Bar Plot"])

        x_axis = st.selectbox("Choose X-axis", df.columns)
        y_axis = st.selectbox("Choose Y-axis", df.columns)

        if plot_type == "Scatter Plot":
            fig, ax = plt.subplots()
            sns.scatterplot(x=x_axis, y=y_axis, data=df, ax=ax)
            st.pyplot(fig)
        elif plot_type == "Line Plot":
            fig, ax = plt.subplots()
            sns.lineplot(x=x_axis, y=y_axis, data=df, ax=ax)
            st.pyplot(fig)
        elif plot_type == "Bar Plot":
            fig, ax = plt.subplots()
            sns.barplot(x=x_axis, y=y_axis, data=df, ax=ax)
            st.pyplot(fig)
        
    else:
        st.write("Please upload a CSV file to create visualizations.")
