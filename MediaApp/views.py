from django.shortcuts import render, get_object_or_404
from MediaApp.forms import UserForm, UserProfileInfoForm, GroupForm, SongForm, EditGroupForm, EditGroupFields, EditSongForm, EditSongFields, AddCommentField
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Group, Song, User, UserProfileInfo, SongComment, SongRating
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages

import requests
import json

# Create your views here.
# Check if user is owner (security)
def userIsOwner(request, user_db):
    if not user_db == request.user:
        raise PermissionDenied
    return True

def index(request):
    return render(request,'MediaApp/index.html')

def profile(request, username):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_login'))
    user_db = User.objects.filter(username = username).first()
    if userIsOwner(request, user_db):
        if not request.user.is_superuser:
            user_db = UserProfileInfo.objects.filter(user = user_db).first()
            comments_by_user = SongComment.objects.filter(user = user_db)[::1]
            comments_by_user.sort(key=lambda x: x.song.id, reverse=True)
            return render(request, 'MediaApp/profile.html', {'user_db' : user_db,
                                                             'comments' : comments_by_user})
        return render(request, 'MediaApp/profile.html', {'user_db' : user_db,})

def delete_user(request, user):
    user = User.objects.filter(username = user).first()
    if userIsOwner(request, user):
        logout(request)
        User.objects.filter(username = user).delete()
        user.delete()
        return HttpResponseRedirect(reverse('index'))

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

def manage(request):
    keywords_gr = {'qs_group': Group.objects.all(), }
    keywords_song = { 'qs_song': Song.objects.all()}
    if request.user.is_superuser:
        if request.method == 'POST':
            group_form = GroupForm(data=request.POST)
            song_form = SongForm(data=request.POST)
            ed_group_form = EditGroupForm(data=request.POST, **keywords_gr)
            ed_song_form = EditSongForm(data=request.POST, **keywords_song)
            if group_form.is_valid():
                group_name = group_form.cleaned_data.get('group_name')
                group_url = group_form.cleaned_data.get('group_url')

                if not Group.objects.filter(name = group_name).filter(url_info = group_url).exists():
                    group_model = Group(name = group_name, url_info = group_url)
                    print(group_model)
                    group_model.save()
            elif ed_group_form.is_valid():
                group = ed_group_form.cleaned_data.get('ed_group')
                return HttpResponseRedirect(reverse('edit_group', kwargs={'pk':group.pk}))

            elif song_form.is_valid():
                song_name = song_form.cleaned_data.get('song_name')
                song_group = song_form.cleaned_data.get('group')
                song_album = song_form.cleaned_data.get('album')
                release_date = song_form.cleaned_data.get('releaseDate')
                genre = song_form.cleaned_data.get('genre')
                song_url = song_form.cleaned_data.get('song_url')
                group_db = Group.objects.filter(name = song_group).first()
                if not group_db:
                    group_db = Group(name = song_group)
                    group_db.save()
                if not Song.objects.filter(name = song_name).filter(group = group_db).exists():
                    song_model = Song(name=song_name, group=group_db, album=song_album, release_date=release_date, genre=genre, url_info=song_url)
                    song_model.save()
            elif ed_song_form.is_valid():
                song = ed_song_form.cleaned_data.get('ed_song')
                return HttpResponseRedirect(reverse('edit_song', kwargs={'pk':song.pk}))

            else:
                print(group_form.errors)
                print(song_form.errors)
        else:
            group_form = GroupForm()
            song_form = SongForm()
            ed_group_form = EditGroupForm(**keywords_gr)
            ed_song_form = EditSongForm(**keywords_song)
        return render(request, 'MediaApp/manage_data.html', {'group_form': group_form,
                                                         'song_form':  song_form,
                                                         'ed_group_form': ed_group_form,
                                                         'ed_song_form': ed_song_form})
    raise PermissionDenied

def edit_group(request, pk):
    if request.user.is_superuser:
        group_model = Group.objects.filter(id=pk).first()
        initial_values={'name': group_model.name, 'url_info': group_model.url_info}
        if request.method == 'POST':
            edit_group_fields_form = EditGroupFields(data=request.POST, initial=initial_values)
            if edit_group_fields_form.is_valid():
                group_model.name = edit_group_fields_form.cleaned_data['name']
                group_model.url_info = edit_group_fields_form.cleaned_data['url_info']
                group_model.save()
        else:
            edit_group_fields_form = EditGroupFields(initial=initial_values)
        return render(request, 'MediaApp/edit_group.html', {'group': group_model,
                                                            'form': edit_group_fields_form})
    raise PermissionDenied

def delete_group(request, pk):
    if request.user.is_superuser:
        Group.objects.filter(id = pk).delete()
        return HttpResponseRedirect(reverse('manage_data'))
    raise PermissionDenied

def edit_song(request, pk):
    if request.user.is_superuser:
        song_model = Song.objects.filter(id=pk).first()
        initial_values={'name': song_model.name, 'group': song_model.group, 'album': song_model.album, 'release_date': song_model.release_date, 'genre': song_model.genre, 'url_info': song_model.url_info}
        if request.method == 'POST':
            edit_song_fields_form = EditSongFields(data=request.POST, initial=initial_values)
            if edit_song_fields_form.is_valid():
                song_model.name = edit_song_fields_form.cleaned_data['name']
                song_model.group = edit_song_fields_form.cleaned_data['group']
                song_model.album = edit_song_fields_form.cleaned_data['album']
                song_model.release_date = edit_song_fields_form.cleaned_data['release_date']
                song_model.genre = edit_song_fields_form.cleaned_data['genre']
                song_model.url_info = edit_song_fields_form.cleaned_data['url_info']
                song_model.save()
        else:
            edit_song_fields_form = EditSongFields(initial=initial_values)
        return render(request, 'MediaApp/edit_song.html', {'song': song_model,
                                                           'form': edit_song_fields_form})

    raise PermissionDenied

def delete_song(request, pk):
    if request.user.is_superuser:
        Song.objects.filter(id = pk).delete()
        return HttpResponseRedirect(reverse('manage_data'))
    raise PermissionDenied

def song_info(request, pk):
    song = Song.objects.filter(pk = pk).first()
    if request.method == 'POST':
        comment_form = AddCommentField(data=request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated and not request.user.is_superuser:
                content = comment_form.cleaned_data.get('content')
                user_db = UserProfileInfo.objects.filter(user = request.user).first()
                comment_db = SongComment(song = song, user = user_db, content = content)
                comment_db.save()
            else:
                return HttpResponse("<script>alert('Can't comment')</script>")
    else:
        comment_form = AddCommentField()
    song_comments = SongComment.objects.filter(song = song)[::1]
    song_ratings = SongRating.objects.filter(song = song)[::1]
    return render(request, 'MediaApp/song_info.html', {'song' : song,
                                                       'comments' : song_comments,
                                                       'comment_form': comment_form,
                                                       'ratings' : song_ratings})

def edit_comment(request, pk):
    comment = SongComment.objects.filter(id = pk).first()
    user = UserProfileInfo.objects.filter(user = request.user).first()
    if comment.user == user:
        initial_values={'content': comment.content}
        if request.method == 'POST':
            comment_form = AddCommentField(data=request.POST, initial = initial_values)
            if comment_form.is_valid():
                comment.content = comment_form.cleaned_data['content']
                comment.save()
                return HttpResponseRedirect(reverse('song_info', kwargs={'pk':comment.song.pk}))
            else:
                print(comment_form.errors)
        else:
            comment_form = AddCommentField(initial = initial_values)
        return render(request, 'MediaApp/edit_comment.html', {'form': comment_form,
                                                              'comment': comment,
                                                              'song': comment.song})
    return HttpResponse("<script>alert('Not owner of this comment')</script>")

def delete_comment(request, pk):
    comment = SongComment.objects.filter(id = pk).first()
    user = UserProfileInfo.objects.filter(user = request.user).first()
    song = comment.song
    if comment.user == user:
        SongComment.objects.filter(id = pk)
        comment.delete()
        return HttpResponseRedirect(reverse('song_info', kwargs={'pk':song.pk}))

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
                           'registered':registered,})

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
                user_db = User.objects.filter(username = username).first()
                print(user_db)
                return HttpResponseRedirect(reverse('profile', kwargs = {'username': user_db.username}))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'MediaApp/login.html', {})

#def song_info(request, pk):
#    song = Song.objects.filter(pk = pk).first()
#    song_comments = SongComment.objects.filter(song = song)[::1]
#    song_ratings = SongRating.objects.filter(song = song)[::1]

    #total = 0
    #counter = 0
    #for rating in song_ratings:
    #    total += ratings
    #    counter += 1
    #average_rating = total/counter

#    return render(request, 'MediaApp/song_info.html', {'song' : song, 'comments' : song_comments, 'ratings' : song_ratings})


def delete_comment(request, pk):
    comment = SongComment.objects.filter(id = pk).first()
    if userIsOwner(request,pk):
        SongComment.objects.filter(id = pk).delete()
        comment.delete()
        return HttpResponseRedirect(reverse('song_info'))
    raise PermissionDenied

#def rate(request, pk):
#    song = get_object_or_404(Song, pk=pk)
#    if SongRating.objects.filter(song=song, user=request.user).exists():
#        SongRating.objects.get(song=song, user=request.user).delete()
#    new_rating = RestaurantReview(rating=request.POST['rating'])
#    new_rating.save()
#    return HttpResponseRedirect(reverse('song_info', args=(song.id,)))

class GroupListView(ListView):
    model = Group

class GroupDetailView(DetailView):
    model = Group
