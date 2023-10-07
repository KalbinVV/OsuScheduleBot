import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

API_URL = os.environ.get('API_URL')

DB_URL = os.environ.get('DB_URL')
