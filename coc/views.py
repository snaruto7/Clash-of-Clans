from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import requests
import json
import os

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'signin.html')

def signup(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                player_info = player()
                player_info.username = request.POST.get('username')
                player_info.player_tag = request.POST.get('player_tag')
                player_info.phone_no = request.POST.get('phone_no')
                player_info.save()
                username = request.POST.get('username')
                password = request.POST.get('password1')            
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        
    return render(request, 'signup.html', {'form' : UserCreationForm()})

@login_required(login_url='signin')
def home(request):
    
    return render(request, 'index.html')

def signout(request):
    logout(request)
    return redirect('signin')