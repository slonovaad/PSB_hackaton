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

    def get_type(self, author: str, letter: str) -> str:
        """Определение категории обращения
        param: author: автор письма
        param: letter: текст письма
        return: ответ LLM (json с определённой категорией обращения)"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_GET_TYPE,
                                           input=f"Отправитель письма: {author}\n Текст письма: {letter}")
        return res.output_text

    def make_answer(self, author: str, person_info: str, letter: str, category: str, is_correct: str, comment: str, routes: str, correspondence_context: str) -> str:
        """Написание ответа на письмо
        param: author: автор письма
        param: person_info: информация об авторе
        param: letter: текст письма
        param: category: категория письма
        param: is_correct: корректность письма с юридической точки зрения
        param: comment: комментарий по наличию противоречий с законодательством или их отсутствии
        param: routes: информация о необходимости перенаправления в другие отделы
        param: correspondence_context: информация о предыдущем контексте переписки с данным отправителем
        return: ответ LLM (json с ответом на письмо)"""
        query = f"""Отправитель письма: {author}\n Информация об авторе: {person_info
        }\n Текст письма: {letter}\n Тип обращения: {category
        }\n Вердикт юриста: обращение {is_correct}\n Противоречия законодательству: {comment
        }\n Перенаправления в другие отделы {routes
        }\n Предыдущая переписка: {correspondence_context}"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_MAKE_ANSWER,
                                           input=query)
        return res.output_text

    def make_routes(self, author: str, person_info: str, letter: str, category: str, is_correct: str, comment: str) -> str:
        """Определение отделов, в которые необходимо перенеправить письмо
        param: author: автор письма
        param: person_info: информация об авторе
        param: letter: текст письма
        param: category: категория письма
        param: is_correct: корректность письма с юридической точки зрения
        param: comment: комментарий по наличию противоречий с законодательством или их отсутствии
        return: ответ LLM (json с перечнем отделов, в которые необходимо перенапрвить, объяснением причины, текстами писем для отделов)"""
        query = f"""Отправитель письма: {author}\n Информация об авторе: {person_info
        }\n Текст письма: {letter}\n Тип обращения: {category
        }\n Вердикт юриста: обращение {is_correct}\n Противоречия законодательству: {comment}\n"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=BANK_EMPLOYEE_INSTRUCTIONS_ROUTE,
                                           input=query)
        return res.output_text
