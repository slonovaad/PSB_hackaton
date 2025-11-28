import os
from dotenv import load_dotenv
from datetime import date

NOW_DATE = date.today().strftime("%d.%m.%Y")
CATEGORIES = ["Запрос информации/документов",
              "Официальная жалоба или претензия",
              "Регуляторный запрос",
              "Партнёрское предложение",
              "Запрос на согласование",
              "Уведомление или информирование"]

load_dotenv()
FOLDER_ID = os.environ['folder_id']
API_KEY = os.environ['api_key']

BASE_URL = "https://rest-assistant.api.cloud.yandex.net/v1"

MODEL = f"gpt://{FOLDER_ID}/yandexgpt/rc"
