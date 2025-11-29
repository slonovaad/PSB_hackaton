from openai import OpenAI
from llm.constants import API_KEY, FOLDER_ID, MODEL, BASE_URL
from llm.llm_bank_employee.bank_employee_constants import BANK_EMPLOYEE_INSTRUCTIONS_GET_TYPE, \
    BANK_EMPLOYEE_INSTRUCTIONS_MAKE_ANSWER, BANK_EMPLOYEE_INSTRUCTIONS_ROUTE


class LlmBankEmployee:
    """Агент-работник банка для взаимодействия с письмами"""

    def __init__(self):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY, project=FOLDER_ID)

    def get_type(self, author, letter) -> str:
        """Определение категории обращения"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_GET_TYPE,
                                           input=f"Отправитель письма: {author}\n Текст письма: {letter}")
        return res.output_text

    def make_answer(self, author, person_info, letter, category, is_correct, comment, routes, correspondence_context) -> str:
        """Написание ответа"""
        query = f"""Отправитель письма: {author}\n Информация об авторе: {person_info
        }\n Текст письма: {letter}\n Тип обращения: {category
        }\n Вердикт юриста: обращение {is_correct}\n Противоречия законодательству: {comment
        }\n Перенаправления в другие отделы {routes
        }\n Предыдущая переписка: {correspondence_context}"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_MAKE_ANSWER,
                                           input=query)
        return res.output_text

    def make_routes(self, author, person_info, letter, category, is_correct, comment) -> str:
        """Написание ответа"""
        query = f"""Отправитель письма: {author}\n Информация об авторе: {person_info
        }\n Текст письма: {letter}\n Тип обращения: {category
        }\n Вердикт юриста: обращение {is_correct}\n Противоречия законодательству: {comment}\n"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_ROUTE,
                                           input=query)
        return res.output_text
