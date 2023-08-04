
from django.apps import AppConfig
class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'
    verbose_name = 'User'
    verbose_name_plural = 'Users'

    """Class representing the configuration of the 'usuario' app."""
    def ready(self):
        pass  # add initialization tasks here