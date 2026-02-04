import os
from dotenv import load_dotenv

def load_config():
    """
    Configuration loader for API keys (if needed).
    NOTE: This project uses Ollama locally and does NOT require API keys.
    This file is kept for potential future integrations only.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # This is okay - Ollama doesn't need API keys
        return None
    return api_key