from django.apps import AppConfig


class AiAgentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_app'

    # def ready(self):
    #     # Ваши инициализационные действия здесь
    #     from .startup import startup_routine
    #     startup_routine()
