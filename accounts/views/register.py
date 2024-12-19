from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from ..models import Registo

def register_user(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')  # Use email as username
        password = request.POST.get('password')

        # Validate all fields
        if not all([nome_completo, idade, sexo, telefone, email, password]):
            messages.error(request, "All fields are mandatory.")
            return redirect('register_user')

        # Check if the user is already registered
        if User.objects.filter(username=email).exists():  # Check if email is already in use
            messages.error(request, "User with this email already exists.")
            return redirect('register_user')

        # Save data to Registo
        registo = Registo.objects.create(
            nome_completo=nome_completo,
            idade=idade,
            sexo=sexo,
            telefone=telefone,
            email=email
        )

        # Create a new user with email as the username
        User.objects.create_user(
            username=email,  # Set email as the username
            password=password
        )

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('welcome_page')

    return render(request, 'accounts/register.html')
