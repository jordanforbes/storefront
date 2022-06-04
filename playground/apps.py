from django.apps import AppConfig
###mosh says taht calling this module apps is misleading and that it should be thought of as a config file instead

class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
