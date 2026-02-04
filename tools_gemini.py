from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import os

def create_agent_gemini(csv_path="healthcare_dataset_cleaned.csv"):
    """
    Create an AI agent using Google Gemini API
    Requires: GOOGLE_API_KEY environment variable
    """
    # Get API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.\n"
            "Get your free API key at: https://makersuite.google.com/app/apikey"
        )
    
    # Load the dataset
    df = pd.read_csv(csv_path)
    
    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        temperature=0,
        convert_system_message_to_human=True
    )
    
    # Create the pandas dataframe agent
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True,
        handle_parsing_errors=True
    )
    
    return agent
