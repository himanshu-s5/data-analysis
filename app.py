import streamlit as st
import home
import data_analysis
import visualization
import about 

st.set_page_config(page_title="Data Analysis App", page_icon="📊", layout="wide")


st.sidebar.title("Navigation")


if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("Data Analysis"):
    st.session_state.page = "Data Analysis"
if st.sidebar.button("Visualization"):
    st.session_state.page = "Visualization"
if st.sidebar.button("About"):
    st.session_state.page = "About"
if "page" not in st.session_state:
    st.session_state.page =  "Home"

if st.session_state.page == "Home":
    home.show()
elif st.session_state.page == "Data Analysis":
    data_analysis.show()
elif st.session_state.page == "Visualization":
    visualization.show()
else:
    about.show()
