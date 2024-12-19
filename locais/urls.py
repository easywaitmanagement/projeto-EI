from django.urls import path
from . import views

urlpatterns = [
    path('', views.locais_page, name='locais'),
    path('session/', views.session_page_redirect, name='session_page_redirect'),
]
