from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('bday',)

class GroupForm(forms.Form):
    # class Meta():
    #     model = Group
    #     fields = ('name',)

    group_name = forms.CharField(label="Group Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Group Name'}))
    group_url = forms.CharField(label="Group URL", max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Group URL'}))

class SongForm(forms.Form):
    song_name = forms.CharField(label="Song Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Song Name'}))
    group = forms.CharField(label="Group", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Group Name'}))
    album = forms.CharField(label="Album", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Album'}))
    releaseDate = forms.CharField(label="Release Date", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Release Date'}))
    genre = forms.CharField(label="Genre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Genre'}))
    song_url = forms.CharField(label="Song URL", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Song URL'}))
