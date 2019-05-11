from django import forms
from .models import UserProfileInfo, Group, Song
from django.contrib.auth.models import User

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

class EditGroupForm(forms.Form):
    ed_group = forms.ModelChoiceField(queryset=Group.objects.none())

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('qs_group')
        super(EditGroupForm, self).__init__(*args, **kwargs)
        self.fields['ed_group'].queryset = qs
        self.fields['ed_group'].empty_label="(No selected)"
        self.fields['ed_group'].label="Group"

class EditGroupFields(forms.ModelForm):
    class Meta():
        model = Group
        exclude = ()

class SongForm(forms.Form):
    song_name = forms.CharField(label="Song Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Song Name'}))
    group = forms.CharField(label="Group", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Group Name'}))
    album = forms.CharField(label="Album", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Album'}))
    releaseDate = forms.CharField(label="Release Date", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Release Date'}))
    genre = forms.CharField(label="Genre", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Genre'}))
    song_url = forms.CharField(label="Song URL", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Song URL'}))

class EditSongForm(forms.Form):
    ed_song = forms.ModelChoiceField(queryset=Group.objects.none())

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('qs_song')
        super(EditSongForm, self).__init__(*args, **kwargs)
        self.fields['ed_song'].queryset = qs
        self.fields['ed_song'].empty_label="(No selected)"
        self.fields['ed_song'].label="Song"

class EditSongFields(forms.ModelForm):
    class Meta():
        model = Song
        exclude = ()

class AddCommentField(forms.Form):
    content = forms.CharField(max_length=500, widget=forms.Textarea)
