# 解決同一層使用無法使用絕對路徑的問題
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from yt_concate_2024.settings import API_KEY
print(API_KEY)
