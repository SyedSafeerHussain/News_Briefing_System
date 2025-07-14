import os
import requests
from dotenv import load_dotenv

# 1. Load environment variables from .env
load_dotenv()
API_KEY=os.getenv("NEWS_API_KEY")
