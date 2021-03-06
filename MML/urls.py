"""MML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from MediaApp import views

app_name= 'MediaApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/(?P<username>\w+)/$',views.profile,name='profile'),
    url(r'^delete_user/(?P<user>\w+)$', views.delete_user, name = 'delete_user'),
    url(r'^generate/$',views.generate,name='generate'),
#    url(r'^generate/$',views.generateSongs,name='generateSongs'),
    url(r'^manage_data/$', views.manage, name= 'manage_data'),


    url(r'^groups/$', views.GroupListView.as_view(), name='Group'),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='Songs_Group'),
    url(r'^songs/(?P<pk>[0-9]+)/$', views.song_info, name='song_info'),
    #url(r'^directors/$', views.DirectorListView.as_view(), name='Director'),
    #url(r'^directors/(?P<pk>[0-9]+)$', views.DirectorDetailView.as_view(), name='Movies_Director'),
    url(r'^edit_group/(?P<pk>[0-9]+)/$', views.edit_group, name= 'edit_group'),
    url(r'^delete_group/(?P<pk>[0-9]+)/$', views.delete_group, name= 'delete_group'),
    url(r'^edit_song/(?P<pk>[0-9]+)/$', views.edit_song, name= 'edit_song'),
    url(r'^delete_song/(?P<pk>[0-9]+)/$', views.delete_song, name= 'delete_song'),
    url(r'^edit_comment/(?P<pk>[0-9]+)/$', views.edit_comment, name= 'edit_comment'),
    url(r'^delete_comment/(?P<pk>[0-9]+)/$', views.delete_comment, name= 'delete_comment'),

]
