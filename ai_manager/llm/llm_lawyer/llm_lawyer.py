from openai import OpenAI
from llm.constants import API_KEY, FOLDER_ID, MODEL, BASE_URL
from llm.llm_lawyer.lawyer_constants import LAWYER_INSTRUCTIONS_CHECK_CORRECTNESS


class LlmLawyer:
    """Агент-юрист для поска юридической информации"""

    def __init__(self):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY, project=FOLDER_ID)

    def check_correctness(self, author: str, letter: str, category: str) -> str:
        """Функция, проверяющая письмо на корректность с юридической точки зрения
        
        param: author: автор письма
        param: letter: текст письма
        param: category: категория письма
        return: ответ LLM (json с вердиктом о корректности письма, комментарием насчёт наличия противоречий с законодательством, перечнем связанных законов, найденной информации об авторе письма)"""
        res = self.client.responses.create(model=MODEL,
                                           instructions=LAWYER_INSTRUCTIONS_CHECK_CORRECTNESS,
                                           input=f"Отправитель (наименование или email): {author}\n Категории: {category}\n Письмо: {letter}", )
        return res.output_text
