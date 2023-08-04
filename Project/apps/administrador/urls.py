from django.urls import path
from .views import login_view

app_name = 'administrador'

urlpatterns = [
    path("login/", login_view, name="login"),
    # Otros patrones de URL para la aplicación "administrador"
]

