from django import forms
from .models import UserProfileInfo
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

class Groupform(forms.Form):
    group_name = forms.CharField(label="Group Name", max_length=100)
    group_url = forms.CharField(label="Group URL", max_length=150)
