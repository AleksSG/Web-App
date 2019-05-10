from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bday = models.DateField(default=date.today)

    def __str__(self):
    	return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=100)
    url_info = models.URLField(max_length=200)

    # def get_name(self):
    #     name = str(self.name)
    #     name = name.lower().replace("'", "").replace("(", "_").replace(")", "_").replace(".", "_").replace(",", "_").replace(" ", "_")
    def get_absolute_url(self):
        return reverse('Songs_Group', args=[str(self.id)])

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    album = models.CharField(max_length=200)
    release_date = models.DateField(default=date.today)
    genre = models.CharField(max_length=50)
    url_info = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class SongComment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    #Only registered users can comment, NOT admin
    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return "On: " + self.song.name

# class Director(models.Model):
#     name = models.CharField(max_length=100)
#
#     def get_absolute_url(self):
#         return reverse('Movies_Director', args=[str(self.id)])
#
#     def __str__(self):
#         return self.name

# class Movie(models.Model):
#     name = models.CharField(max_length=100)
#     director = models.ForeignKey(Director, on_delete=models.CASCADE)
#     release_date = models.DateField(default=date.today)
#     genre = models.CharField(max_length=50)
#     description = models.CharField(max_length=2000)
#     url_info = models.URLField(max_length=200)
#
#     def __str__(self):
#     	return self.name
#
#     def create(cls,n,d,rD,g,descr,url):
#         movie = cls(name=n, director=d, releaseDate=rD, genre=g, description=descr, url_info=url)
#         return movie
