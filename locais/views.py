from django.shortcuts import render, redirect

def locais_page(request):
    return render(request, 'locais/locais.html')


def session_page_redirect(request):
    # Redirect to the session_page view in user_sessions
    image_url = request.GET.get('image')  # Get the image path from the query string
    if image_url:
        return redirect(f'/user_sessions/session/?image={image_url}')
    else:
        return redirect('/user_sessions/session/')