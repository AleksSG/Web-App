from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Director(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre= models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    url_info = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bday = models.CharField(max_length=20)
    
    def __str__(self):
    	return self.user.username

