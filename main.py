import streamlit as st
import pandas as pd
from data_upload import upload_csv, connect_google_sheet
from webScrap import web_search, getdata_from_url
from llmChat import perform_chat

def main():
    # Streamlit page configuration
    st.set_page_config("Info Harvester AI")
    st.title("Info Harvester AI")
    st.subheader("Data Source Selection")

    # Allow user to select data source
    data = st.radio(
        "Select the data source:",
        ("CSV", "Google Sheet")
    )

    df = None
    if data == "CSV":
        df = upload_csv()
        # st.write(df.head(5))
        if df is not None:
            col_name = st.text_input("Enter the name of the selected column: ")
            if col_name in df.columns:
                st.write(df[col_name].head(5))  # Preview first 5 values of the column
                col_list = df[col_name].tolist()  # Convert column to list

                query = st.text_input("Enter the query you want to ask: ")

                answer = []
                if query:
                    for col in col_list:
                        link = web_search(col)  # Search the web for the column name
                        if link:  # If a link is found
                            raw_text = getdata_from_url(link)
                            if raw_text:  # If content is successfully fetched
                                output = perform_chat(raw_text, query)
                                answer.append(output)
                            else:  # If there was an issue fetching data
                                answer.append(None)
                        else:  # If no link is found
                            answer.append(None)

                    result_df = pd.DataFrame({"Selected_column": col_list, "Output": answer})
                    st.write(result_df)

                    # Add a download button for the CSV
                    csv = result_df.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name="output.csv",
                        mime="text/csv"
                    )
            else:
                st.write("No such column present in the CSV file")

    elif data == "Google Sheet":
        url = st.text_input("Enter the URL of GOOGLE SHEET: ")
        if url:
            if "docs.google.com/spreadsheets" in url:
                df = connect_google_sheet(url)
                if df is not None:
                    st.write(df.head(5))  # Preview first 5 rows of the data

                    col_name = st.text_input("Enter the name of the selected column: ")
                    if col_name in df.columns:
                        st.write(df[col_name].head(5))  # Preview first 5 values of the column
                        col_list = df[col_name].tolist()  # Convert column to list

                        query = st.text_input("Enter the query you want to ask: ")

                        answer = []
                        if query:
                            for col in col_list:
                                link = web_search(col)  # Search the web for the column name
                                if link:  # If a link is found
                                    raw_text = getdata_from_url(link)
                                    if raw_text:  # If content is fetched successfully
                                        output = perform_chat(raw_text, query)
                                        answer.append(output)
                                    else:  # If there was an issue with content fetching
                                        answer.append(None)
                                else:  # If no link is found
                                    answer.append(None)

                            result_df = pd.DataFrame({"Selected_column": col_list, "Output": answer})
                            st.write(result_df)

                            # Add a download button for the CSV
                            csv = result_df.to_csv(index=False)
                            st.download_button(
                                label="Download CSV",
                                data=csv,
                                file_name="output.csv",
                                mime="text/csv"
                            )

                    else:
                        st.write("No such column present in the Google Sheet")
    else:
        st.write("Please choose a valid data source")

if __name__ == "__main__":
    main()
