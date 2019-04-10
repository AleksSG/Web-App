# Web-App

A Group Project which consists in creating the background of a Web using Django.

### Motivation

We are asked to do a project from _Universitat de Lleida_ subject 'Project Web'.

### Application idea

We will make a kind of media database which includes music, movies, etc. using the [iTunes API](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) without affiliating where the user can search content in our D.B. and it will be shown all the information about the result.
The user can sing up and log in to a personal space with its information and some additional functionalities such as:

* Creating playlists
* Possibility to rate the media
* Possibility to comment the media
* Send private messages between other users
* Create their own playlists
* Mark the media with a status
    * Plan to listen/watch
    * Currently watching
    * Completed

Moreover, we will use a Free API such as YouTube or SoundCloud to allow the possibility to reproduce the content.

### Contributors
* Albert Planes - [Github: Apseuma](http://github.com/Apseuma)
* Aleks Genov - [Github: AleksSG](http://github.com/AleksSG)
* Miquel Ribes - [Github: mikiribe14](http://github.com/mikiribe14)
* Paula Vicente - [Github: paulavicente98](http://github.com/paulavicente98)
* Sergio Vargas - [Github: sergiovargaspuy](http://github.com/sergiovargaspuy)

### Considerations for the 1st delivery
The user has to press the button "Fill database from iTunes API" for fill the application database with songs, movies, directors and groups. All the content is extracted from the iTunes API.

In this case, we just get the songs from a few groups (Melendi, Els amics de les arts, Ariana Grande, Miley Cyrus, Shawn Mendes, Ed Sheeran i Vicetone). Refering to the movies, we just get the movies from a few directors (Martin Scorsese, Joe Russo, Tim Burton, Quentin Tarantino  and Steven Spielberg)

Showing the songs of a group (or the movies of a director) is not implemented yet, but they can be seen from the django admin interface

If the user is not logged, the navbar shows the "Register" and "Log in" buttons. If the user is logged, the navbar shows the "Logout" and "MyProfile" buttons.

User: admin
Password: admin
