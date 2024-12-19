from django.shortcuts import render, redirect
from .models import Registo, Users
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        # Check if the user is already registered
        if Registo.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect('register_user')

        # Save data to Registo and Users
        registo = Registo.objects.create(
            nome_completo=nome_completo,
            idade=idade,
            sexo=sexo,
            telefone=telefone,
            email=email
        )
        user = Users.objects.create(
            registo=registo,
            user=nome_completo[:3] + str(registo.id),
            palavra_passe='password123'  # Replace with generated password mudar isto wtf
        )
        messages.success(request, f"Registered successfully! Username: {user.user}, Password: password123")
        return redirect('login')

    return render(request, 'accounts/register.html')


