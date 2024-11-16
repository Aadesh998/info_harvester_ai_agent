import os
import serpapi
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader

# Load environment variables from .env file
load_dotenv()

# Get API keys from the environment
api_key = os.getenv('SERPAPI_KEY')
client = serpapi.Client(api_key = api_key)

def getdata_from_url(url):
    """Function to fetch content from a URL using WebBaseLoader"""
    try:
        # Load data from the URL
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content
        content = page_data.replace("\n", " ").replace("\r", " ")
        content = content[:6000]  # Limit content length to 6000 characters
        return content
    except Exception as e:
        # st.error(f"Error fetching data from the URL: {url}.\nError: {str(e)}")
        return None

def web_search(name):
    """Perform a Google search using SerpAPI and return the first result link"""
    try:
        results = client.search(
            q=name,
            engine="google",
            location="India",
            hl="en",
            gl="us",
            num=1,
        )
        # Return the first link found in organic results
        for item in results.get("organic_results", []):
            return item["link"]
        return None
    except Exception as e:
        # st.error(f"Error performing search for '{name}'.\nError: {str(e)}")
        return None