# Info Harvester AI

## Project Summary
Info Harvester AI is a data processing and analysis tool that leverages Streamlit for the interface, LangChain for natural language processing, and SerpAPI for web searches. The tool allows users to upload data from CSV files or Google Sheets, perform web searches, and extract specific information using advanced AI models. It generates a downloadable CSV report containing the extracted insights.

## Key Features
* Upload and Process CSV Files: Easily upload CSV files and extract insights from specific columns.
* Google Sheets Integration: Connect to Google Sheets via a URL to fetch data and perform analysis.
* Web Scraping: Search the web using SerpAPI and extract relevant information.
* AI-Powered Information Extraction: Utilize Llama-based models for natural language processing and specific data extraction.
* Downloadable Reports: Export results as a CSV file for further use.

## Project Structure

InfoHarvesterAI/ │ ├── app.py # Main Streamlit application ├── data_upload.py # Module for CSV and Google Sheet data upload ├── llmChat.py # AI model integration and prompt handling ├── webScrap.py # Web scraping and search functions ├── requirements.txt # Dependencies for the project ├── .env # Environment variables └── README.md # Documentation (this file)
