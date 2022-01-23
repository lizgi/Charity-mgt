from django.apps import AppConfig


class CharappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charapp'
def ready(self):
        import charapp.signals
