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
import time


headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM4MWMwNjFkLTYxY2EtNDcyNC04ODAzLWY3YjZiY2FiMDEzZSIsImlhdCI6MTU5NzI0Mzc2NSwic3ViIjoiZGV2ZWxvcGVyLzQ5ZWNiNGFkLTcwMjQtNDcxMy03NWE1LTdlOWNjNjJlMGY4ZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjUyLjE3LjE1Ni4xMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.G8toqzSjq5PR_6SeUufwWDDtCngspw7BkNHY3TMzo7ns9sSu1yoGbwF2c8SuJ-yqgbZfbWA3iabdU-6Yp7OkCQ',
    'Accept': 'application/json'
}

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
        start_time = time.time()
        form = UserCreationForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                player_info = player()
                player_info.username = request.POST.get('username')
                player_info.player_tag = request.POST.get('player_tag')
                player_info.phone_no = request.POST.get('phone_no')

                player_info_url = 'https://api.clashofclans.com/v1/players/%23' + request.POST.get('player_tag')
                print(player_info_url)
                response = requests.get(player_info_url, headers=headers, verify=False)
                player_json = response.json()
                print(player_json)
                player_info.clan = player_json['clan']['name']
                player_info.role = player_json['role']
                player_info.attackWins = player_json['attackWins']
                player_info.defenseWins = player_json['defenseWins']
                player_info.townHallLevel = player_json['townHallLevel']
                player_info.versusBattleWins = player_json['versusBattleWins']
                player_info.expLevel = player_json['expLevel']
                player_info.trophies = player_json['trophies']
                player_info.bestTrophies = player_json['bestTrophies']
                player_info.donations = player_json['donations']
                player_info.donationsReceived = player_json['donationsReceived']
                player_info.builderHallLevel = player_json['builderHallLevel']
                player_info.versusTrophies = player_json['versusTrophies']
                player_info.bestVersusTrophies = player_json['bestVersusTrophies']
                player_info.warStars = player_json['warStars']
                player_info.versusBattleWinCount = player_json['versusBattleWinCount']
                form.save()
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