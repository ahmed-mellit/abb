import streamlit as st
import pandas as pd
from checking_functions.bolean_check import verify_boolean_column

# Page for verifying boolean column
def page_verify_boolean_column():
    st.title("Verify Boolean Column")
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        column_name = st.text_input("Enter Column Name")

        if st.button("Verify Boolean Column"):
            if column_name not in df.columns:
                st.error(f"Column '{column_name}' not found in the Excel file.")
            else:
                incorrect_values = verify_boolean_column(df, column_name)
                st.write("IDs with Incorrect Boolean Values:", incorrect_values)
