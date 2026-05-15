import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CSV Insight Pro",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CSV Insight Pro")
st.write("A simple and professional CSV data analysis dashboard.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("CSV file uploaded successfully!")

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Duplicates", df.duplicated().sum())

    st.subheader("Data Preview")
    st.dataframe(df.head(10))

    st.subheader("Column Information")
    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(column_info)

else:
    st.info("Please upload a CSV file to start.")

         
