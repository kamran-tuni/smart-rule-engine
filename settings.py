import os
from dotenv import load_dotenv

load_dotenv()

AI_API_KEY = os.getenv('AI_API_KEY')
IoT_PLATFORM_API_KEY = os.getenv('IoT_PLATFORM_API_KEY')
IoT_PLATFORM_BASE_URL = os.getenv('IoT_PLATFORM_BASE_URL')
