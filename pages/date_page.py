import streamlit as st
import pandas as pd
from checking_functions.date_check import verify_date_format

# Page for verifying date format
def page_verify_date_format():
    st.title("Verify Date Format")
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        column_name = st.text_input("Enter Column Name")
    
        if st.button("Verify Date Format"):
            if column_name not in df.columns:
                st.error(f"Column '{column_name}' not found in the Excel file.")
            else:
                incorrect_dates = verify_date_format(df, column_name)
                st.write("IDs with Incorrect Date Format:", incorrect_dates)
