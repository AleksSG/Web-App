from django.shortcuts import render
from MediaApp.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Group, Director, Movie, Song

import requests
import json

# Create your views here.
def index(request):
    return render(request,'MediaApp/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#def generate(request): #movie
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
#    return render(request,'MediaApp/generate.html')


def generate(request): #songs
    groups=['Vicetone','Melendi','Els amics de les arts','Miley Cyrus','Ariana Grande','Ed Sheeran', 'Shawn Mendes']
    for group in groups:
        lowgroup=group.lower()
        lowgroup=lowgroup.replace(" ", "+")

        a = 'https://itunes.apple.com/search?entity=song&term='
        a = a + lowgroup
        b = requests.get(a).json()
        #pelis=json.dumps(b, indent=2)
        songs=b['results']

        artUrl=''
        bool=0
        for i in songs:
            if ('artistViewUrl' in i) and (bool==0):
                artUrl=i['artistViewUrl']
                bool=1

        gr = Group(name = group, url_info = artUrl)
        gr.save()

        for i in songs:
            alb=''
            if 'collectionName' in i:
                alb = i['collectionName']

            son = Song(name= i['trackName'], group = gr, album = alb, release_date= i['releaseDate'][:10], genre= i['primaryGenreName'], url_info= i['trackViewUrl'])
            son.save()

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
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

class DirectorListView(generic.ListView):
    model = Director

class MovieListView(generic.DetailView):
    model = Movie

class SongListView(generic.DetailView):
    model = Song
