from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'callisto.users_app'

    def ready(self):
        import callisto.users_app.signals
