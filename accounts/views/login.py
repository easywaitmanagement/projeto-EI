from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # Replace 'username' with 'email'
        password = request.POST.get('password')

        # Authenticate the user using email as username
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, "Login successful!")
            return redirect('locais')  # Redirect to the session page
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login_user')

    return render(request, 'accounts/log-in.html')

@login_required
def locais_page(request):
    return render(request, 'locais/locais.html')