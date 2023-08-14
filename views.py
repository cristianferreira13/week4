from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'base/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('home')  # Redirect to your home page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})

def login_view(request):
    
    return render(request, 'base/login.html')

