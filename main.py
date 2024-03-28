import streamlit as st
from pages.bolean_page import page_verify_boolean_column
from pages.date_page import page_verify_date_format
from pages.required_page import page_missing_records

# Main function to run the Streamlit app
def main():
    st.sidebar.title("Menu")
    menu_options = ["Find Missing Records", "Verify Date Format", "Verify Boolean Column"]
    page = st.sidebar.selectbox("Select Page", menu_options)
    
    if page == "Find Missing Records":
        page_missing_records()
    elif page == "Verify Date Format":
        page_verify_date_format()
    elif page == "Verify Boolean Column":
        page_verify_boolean_column()


if __name__ == "__main__":
    main()
