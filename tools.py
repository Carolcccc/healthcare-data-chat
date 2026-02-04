from langchain_ollama import ChatOllama
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

def create_agent(csv_path="healthcare_dataset_cleaned.csv"):
    # No API key needed for local execution!
    df = pd.read_csv(csv_path)
    
    # Initialize Llama 3.2 on your M4
    llm = ChatOllama(
        model="llama3.2", 
        temperature=0
    )
    
    agent = create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True, 
        allow_dangerous_code=True
    )
    return agent