from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

# Create your views here.
def proyecto_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect ('home')
    
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def proyecto_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    context = {
        'user': request.user,
        'profile': profile,
    }
    return render(request, 'registration/profile.html', context)

@login_required
def proyecto_logout_view(request):
    logout(request)
    return redirect('home')
