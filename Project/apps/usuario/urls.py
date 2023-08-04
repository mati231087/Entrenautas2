from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil_view, name='perfil'),
    # Otros patrones de URL para la aplicación "usuario"
]