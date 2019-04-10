from django.contrib import admin
from .models import UserProfileInfo, User, Group, Director, Movie, Song
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Movie)
admin.site.register(Song)
admin.site.register(Director)
admin.site.register(Group)
