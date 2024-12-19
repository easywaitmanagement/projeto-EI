from .register import register_user
from .login import login_user
from django.shortcuts import render

def welcome_page(request):
    return render(request, 'accounts/welcome-page.html')