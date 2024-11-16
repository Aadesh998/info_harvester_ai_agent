import streamlit as st 
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def upload_csv():
    """Function to upload a CSV file"""
    file_upload = st.file_uploader("Upload a csv file", type=["csv"])
    if file_upload is not None:
        df = pd.read_csv(file_upload)
        st.dataframe(df.head(5))
        return df  # Return DataFrame
    else:
        st.write("Please upload the CSV file")
    return None

def connect_google_sheet(url):
    """Connect to Google Sheets and read the data"""
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        data = conn.read(spreadsheet=url)
        return data
    except Exception as e:
        # st.error(f"Error reading the Google Sheet: {url}.\nError: {str(e)}")
        return None