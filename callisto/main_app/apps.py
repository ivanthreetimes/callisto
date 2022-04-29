from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callisto.main_app'

    def ready(self):
        from callisto.main_app import signals
