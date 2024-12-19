import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Senhas

@login_required
def session_page(request):
    generated_number = None

    # Update or retrieve the image from the session
    image_url = request.GET.get('image')  # Check if a new image was selected
    if image_url:
        request.session['selected_image'] = image_url  # Store the selected image in the session
    else:
        image_url = request.session.get('selected_image')  # Retrieve the stored image from the session

    if request.method == 'POST':  # Handle "Gerar Senha" button click
        generated_number = f"{random.randint(0, 9999):04d}"  # Generate a random 4-digit number
        Senhas.objects.create(user=request.user, number=generated_number)  # Save the number

    return render(request, 'user_sessions/session-page.html', {
        'generated_number': generated_number,
        'image_url': image_url,  # Pass the image URL to the template
    })



@login_required
def senhas_page(request):
    # Fetch the latest generated number for the logged-in user
    latest_senha = Senhas.objects.filter(user=request.user).order_by('-created_at').first()

    return render(request, 'user_sessions/senhas-page.html', {
        'latest_senha': latest_senha.number if latest_senha else None,
    })

