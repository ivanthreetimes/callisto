from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callisto.users_app'

    def ready(self):
        from callisto.users_app import signals
