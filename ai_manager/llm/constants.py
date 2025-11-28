import os
from dotenv import load_dotenv


load_dotenv()
FOLDER_ID = os.environ['folder_id']
API_KEY = os.environ['api_key']

BASE_URL = "https://rest-assistant.api.cloud.yandex.net/v1"

MODEL = f"gpt://{FOLDER_ID}/yandexgpt/rc"

BANK_EMPLOYEE_INSTRUCTIONS = """Ты - сотрудник банка ПСБ.
Ты ведёшь деловую переписку с партнёрами и клиентами.
Тебе требуется корректно отвечать на письма, соблюдая нужный стиль.
Тебе на вход подаётся деловое письмо, ты же должен на него ответить юридически и
профессионально корректно, соблюдая стиль, соответствующий стилю поступившего письма"""