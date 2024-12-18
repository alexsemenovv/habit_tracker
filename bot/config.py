import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к. отсутствует фал .env')
else:
    load_dotenv()

TOKEN = os.getenv("TOKEN")

