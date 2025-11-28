from llm.constants import NOW_DATE, CATEGORIES

EXAMPLES = ""
with open("llm\examples.txt", encoding="utf-8") as f:
    EXAMPLES = f.read()
BASE_PROMPT = ""
with open("llm\prompt.txt", encoding="utf-8") as f:
    BASE_PROMPT = f.read()

BANK_EMPLOYEE_INSTRUCTIONS = f"""{BASE_PROMPT}

Пиши сырым текстом без markdown-разметки
Ответ должен быть дан в корректном формате json без дополнительных символов. Напиши только
сырой текст json-файла без дополнительных символов
Поля в json-файле:
deadline - дата, до которой ориентировочно должен быть дан ответ - дата в формате дд.мм.гггг. (сегодняшняя дата: {NOW_DATE})
answer - финальный текст ответного письма на русском языке без markdown-разметки. Вся информация должна быть уже заполнена.
type - типы обращения, к которым пожно отнести письмо. Список из одного или нескольких значений из набора: {CATEGORIES}

Примеры распределения писем по типам обращения и ответов на письма:
{EXAMPLES}
"""
