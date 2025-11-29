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

ROUTES = {"support": ["Служба поддержки клиентов", "Undefined"],
          "claim": ["Отдел претензий и разбирательств", "Undefined"],
          "tech": ["Техническая поддержка IT", "Undefined"],
          "law": ["Юридический отдел", "Undefined"],
          "security": ["Отдел безопасности", "Undefined"],
          "cooperate": ["Департамент корпоративного бизнеса", "Undefined"],
          "marketing": ["Департамент маркетинга и PR", "Undefined"],
          "charity": ["Отдел благотворительности и ESG", "Undefined"],
          "secretary": ["Канцелярия/Секретариат", "Undefined"],}

load_dotenv()
FOLDER_ID = os.environ['folder_id']
API_KEY = os.environ['api_key']

BASE_URL = "https://rest-assistant.api.cloud.yandex.net/v1"

MODEL = f"gpt://{FOLDER_ID}/yandexgpt/rc"
