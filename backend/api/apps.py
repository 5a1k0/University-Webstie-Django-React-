from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'api'

    def ready(self):
        print("AppConfig ready method called.")
        import api.signals