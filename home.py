import streamlit as st

def show():
    st.title("Welcome to the Data Analysis App")
    
    st.write("""
        This app provides a comprehensive platform for performing data analysis and creating visual insights from your datasets. 
        You can upload your own data in CSV format, analyze it, and visualize trends and patterns using a range of plotting options.
    """)
    
    st.header("Features of the App")
    
    st.subheader("1. Data Analysis")
    st.write("""
        - Upload your dataset in CSV format.
        - Automatically generate summary statistics like mean, median, standard deviation, etc.
        - View the raw data in a table format for easy inspection.
        - Explore the structure of your dataset, including the columns and data types.
        - Analyze individual features or relationships between features.
    """)
    
    st.subheader("2. Data Visualization")
    st.write("""
        - Create interactive visualizations to explore your data further.
        - Choose from several types of charts: scatter plots, line plots, bar charts, and more.
        - Customize your plots by selecting specific columns for the X and Y axes.
        - Visualizations are generated using the powerful Seaborn and Matplotlib libraries for quality and flexibility.
    """)
    
    st.subheader("3. User-Friendly Interface")
    st.write("""
        - Simple navigation between different pages: Home, Data Analysis, Visualization, and About.
        - Upload datasets with a single click and analyze them immediately.
        - Customize visualizations easily using intuitive controls.
    """)
    
    st.subheader("4. About")
    st.write("""
        Learn more about the technical details of the app, the technologies used, and the developer's contact information.
    """)
    
    st.header("How to Use the App")
    
    st.write("""
    1. **Upload Data**: Start by going to the **Data Analysis** page and upload a CSV file.
    2. **Explore Data**: View the dataset and see summary statistics.
    3. **Create Visualizations**: Go to the **Visualization** page to create charts from the dataset.
    4. **Learn More**: Visit the **About** section to get information about the app and its development.
    """)
    
    st.header("Technologies Used")
    
    st.write("""
    This app is built with the following technologies:
    
    - **Streamlit**: A Python framework for building web apps quickly and easily.
    - **Pandas**: Used for data manipulation and analysis.
    - **Seaborn** and **Matplotlib**: Libraries for creating static, animated, and interactive visualizations.
    """)
    
    st.info("Note: The app supports only CSV file uploads at this time. Future versions may include support for other formats.")
