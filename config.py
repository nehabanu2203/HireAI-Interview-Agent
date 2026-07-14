import os
from dotenv import load_dotenv

# Get the directory where this config.py file is located
current_dir = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(current_dir, ".env")

# Load .env file
load_dotenv(env_file_path)

# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"