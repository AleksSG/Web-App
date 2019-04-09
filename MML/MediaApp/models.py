from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    url_info = models.URLfield(max_length=200)
    
    def __str__(self):
        return self.name

class Director(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    release_date = models.DateField(default=date.today)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    url_info = models.URLfield(max_length=200)

    def __str__(self):
    	return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    album = models.CharField(max_length=200)
    release_date = models.DateField(default=date.today)
    genre = models.CharField(max_length=50)
    url_info = models.URLfield(max_length=200)

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bday = models.DateField(default=date.today)
    
    def __str__(self):
    	return self.user.username

