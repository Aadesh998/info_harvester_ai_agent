import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load a llama model
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"), model_name = "llama-3.1-70b-versatile")

def perform_chat(page_data ,query):
    """Function to extract data based on the query from the scraped text using a prompt"""
    prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the website.
        Your job is to extract the {query}
        ### VALID OUTPUT (NO PREAMBLE):    
        """
    )

    chain_extract = LLMChain(prompt=prompt_extract, llm=llm)

    # Run the chain to extract the information
    res = chain_extract.run({"page_data": page_data, "query": query})

    # Return the result (extracted answer)
    return res