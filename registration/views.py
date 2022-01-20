from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .utils import NewUserForm


def register_page(request):
    """Saves new users to database"""

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a bien été crée!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_page(request):
    """Logs a user in"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Erreur d\'authentidication! Nom '
                          ' d\'utilisateur ou mot de passe incorrect.')
    context = {}
    return render(request, 'registration/login.html', context)


def logout_user(request):
    """Logs a user out"""

    logout(request)
    return redirect('homepage')
