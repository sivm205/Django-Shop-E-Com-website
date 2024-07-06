from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import shop 

def home(request):
    return render(request, 'shop/home.html')

def shop_list(request):
    shops = shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shops': shops})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})


def logout(request):
    return render(request, 'shop/logout.html')





