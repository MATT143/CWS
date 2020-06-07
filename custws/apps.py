from django.apps import AppConfig


class CustwsConfig(AppConfig):
    name = 'custws'

    def ready(self):
        import custws.signals