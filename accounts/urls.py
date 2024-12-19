from django.urls import path
from .views import register_user, login_user, welcome_page

urlpatterns = [
    path('', welcome_page, name='welcome_page'),  # Route for the welcome page
    path('register/', register_user, name='register_user'),  # Route for sign in
    path('login/', login_user, name='login_user'),  # Route for log in
]
