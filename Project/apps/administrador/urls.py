
from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='admin_login'),
]