import streamlit as st
import pandas as pd
from checking_functions.required_check import find_missing_records

# Page for finding missing records
def page_missing_records():
    st.title("Find Missing Records")
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        column_name = st.text_input("Enter Column Name")

        if st.button("Find Missing Records"):
            if column_name not in df.columns:
                st.error(f"Column '{column_name}' not found in the Excel file.")
            else:
                missing_records = find_missing_records(df, column_name)
                st.write("Missing IDs:", missing_records)
