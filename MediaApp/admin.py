from django.contrib import admin
from .models import UserProfileInfo, User, Group, Song, SongComment, SongRating
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(SongComment)
admin.site.register(Song)
admin.site.register(Group)
admin.site.register(SongRating)
