from django.shortcuts import render
from MediaApp.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Group, Song

import requests
import json

# Create your views here.
def index(request):
    return render(request,'MediaApp/index.html')

def profile(request, username):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_login'))
    return render(request, 'MediaApp/profile.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# def generateMovies(request): #movie
#    directors=['Tim Burton','Martin Scorsese','Steven Spielberg','Joe Russo','Quentin Tarantino']
#    for director in directors:
#        direc = Director(name= director)
#        direc.save()
#
#        director=director.lower()
#        director=director.replace(" ", "+")
#
#        a = 'https://itunes.apple.com/search?entity=movie&term='
#        a = a + director
#        b = requests.get(a).json()
#        #pelis=json.dumps(b, indent=2)
#        pelis=b['results']
#        for i in pelis:
#            d=''
#            if 'shortDescription' in i:
#                d = i['shortDescription']
#
#            mov = Movie(name= i['trackName'], director= direc, release_date= i['releaseDate'][:10], genre= i['primaryGenreName'], description= d, url_info= i['trackViewUrl'])
#            mov.save()
#            #print(pelis[i]['longDescription']+" - ",end="")
#
#    #return render(request,'MediaApp/generate.html')

def generateSongs(request): #songs
    groups=['Vicetone','Melendi','Els amics de les arts','Miley Cyrus','Ariana Grande','Ed Sheeran', 'Shawn Mendes']
    groups_db = Group.objects.all()
    for group in groups:

        query = 'https://itunes.apple.com/search?entity=song&term=' + group.lower().replace(" ", "+")
        response = requests.get(query).json()

        songs = response['results']

        artUrl=''
        for song in songs:
            if 'artistViewUrl' in song:
                artUrl= song['artistViewUrl']
                break
        #Check if in DB
        group_model = None
        if not Group.objects.filter(name = group).exists():
            group_model = Group(name = group, url_info = artUrl)
            group_model.save()
        else:
            group_model = Group.objects.filter(name = group).first()

        songs_db = Song.objects.filter(group = group_model)
        for song in songs:
            song_model = None
            if not Song.objects.filter(group = group_model).filter(name = song['trackName']).exists():
                alb=''
                if 'collectionName' in song:
                    alb = song['collectionName']
                song_model = Song(name= song['trackName'], group = group_model, album = alb, release_date= song['releaseDate'][:10], genre= song['primaryGenreName'], url_info= song['trackViewUrl'])
                song_model.save()
            else:
                song_model = Song.objects.filter(group = group_model).filter(name = song['trackName']).first()


def generate(request):
    generateSongs(request)
    #generateMovies(request)
    return render(request,'MediaApp/generate.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'MediaApp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profile'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('profile', kwargs = {'username': username}))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'MediaApp/login.html', {})

class GroupListView(generic.ListView):
    model = Group

class GroupDetailView(generic.DetailView):
    model = Group
