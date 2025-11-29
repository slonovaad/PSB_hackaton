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

ROUTES = {"support": ["Служба поддержки клиентов", "superjorik2020@gmail.com"],
          "claim": ["Отдел претензий и разбирательств", "vikabaz2007@gmail.com"],
          "tech": ["Техническая поддержка IT", "hayko5687@gmail.com"],
          "law": ["Юридический отдел", "haykosteam@gmail.com"],
          "security": ["Отдел безопасности", "haykmechanic@gmail.com"],
          "cooperate": ["Департамент корпоративного бизнеса", "mai.slonovaad@gmail.com"],
          "marketing": ["Департамент маркетинга и PR", "hkeesteam@gmail.com"],
          "charity": ["Отдел благотворительности и ESG", "hkeesteam9685@gmail.com"],
          "secretary": ["Канцелярия/Секретариат", "hharmen007@gmail.com"],}

load_dotenv()
FOLDER_ID = os.environ['folder_id']
API_KEY = os.environ['api_key']

BASE_URL = "https://rest-assistant.api.cloud.yandex.net/v1"

MODEL = f"gpt://{FOLDER_ID}/yandexgpt/rc"
