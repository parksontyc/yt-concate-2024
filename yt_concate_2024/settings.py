import os
from dotenv import load_dotenv

load_dotenv()  # 從.env載入api key
API_KEY = os.getenv('API_KEY')  # 拿到key
