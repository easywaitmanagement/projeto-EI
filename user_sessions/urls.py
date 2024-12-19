from django.urls import path
from .views import session_page, senhas_page

urlpatterns = [
    path('session/', session_page, name='session_page'),
    path('senhas/', senhas_page, name='senhas_page'),
]
