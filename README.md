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

![image](https://github.com/user-attachments/assets/c0ae1258-340e-43d4-b869-422f76e41800)

## Setup Instructions
### Prerequisites
* Python 3.8 or higher
* A Google account to access Google Sheets
* API keys for:
  * Groq for LangChain model integration
  * SerpAPI for web search
 
### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Aadesh998/info_harvester_ai_agent.git
   ```
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   * Create a .env file in the root directory.
   * Add the following keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   SERPAPI_KEY=your_serpapi_key
   ```

### Running the Application
Run the Streamlit app locally:
```
streamlit run main.py
```

### Usage Guide
1. Select Data Source:
   Upload a CSV file or connect to a Google Sheet.
2. Select Column:
   Choose the column to analyze.
3. Enter Query:
   Input a query to extract specific information from web-scraped data.
4. View and Download Results:
   Preview the extracted insights and download them as a CSV file.

### Third-Party Tools & APIs
1. Streamlit: For creating the interactive web application.
2. LangChain: For AI-based natural language processing and information extraction.
3. groq: For AI model fast infrence.
4. SerpAPI: For Google search results and web scraping.
5. Pandas: For data manipulation and analysis.
   
### Future Enhancements
1. Add more data sources (e.g., databases, APIs).
2. Integrate additional AI models for better data insights.
3. Improve error handling and logging.
   
### Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
