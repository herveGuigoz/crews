#!/usr/bin/env python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import warnings

from crews.crew import RecipeFromYoutubeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI LLM
default_llm = ChatOpenAI(
    openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    temperature=0.1,
    model_name=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
    top_p=0.3
)

def run():
    """
    Run the crew.
    """
    inputs = {
        'video_id': 'E2L3bQKow3U',  # Replace with actual YouTube video ID
        'languages': ['fr', 'en', 'it']  # Language codes to try for transcript
    }

    try:
        RecipeFromYoutubeCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
