from django.apps import AppConfig


class EdetcapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edetcap'

    def ready(self):
        import edetcap.signals
