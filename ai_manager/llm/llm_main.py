from openai import OpenAI
from llm.constants import API_KEY, FOLDER_ID, MODEL, BASE_URL, BANK_EMPLOYEE_INSTRUCTIONS


def llm_bank_employee(query):
    client = OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY, project=FOLDER_ID)
    res = client.responses.create(model=MODEL,
                                  instructions=BANK_EMPLOYEE_INSTRUCTIONS,
                                  input=query)
    return res.output_text