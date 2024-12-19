from django.urls import path
from .views import print_senha

urlpatterns = [
    path('print/', print_senha, name='print_senha'),
]
