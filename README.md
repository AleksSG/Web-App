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

## Considerations for the 1st delivery

### Data model documentation
The entities are defined in the /MML/MediaApp/models.py file.
This entities are: Group, Director, Movie, Song and UserProfileInfo

### General considerations of the application

The user has to press the button "Fill database from iTunes API" for filling the application database with songs, movies, directors and groups. All the content is extracted from the iTunes API.

In this case, we just get the songs from a few groups (Melendi, Els amics de les arts, Ariana Grande, Miley Cyrus, Shawn Mendes, Ed Sheeran and Vicetone). Refering to the movies, we just get the movies from a few directors (Martin Scorsese, Joe Russo, Tim Burton, Quentin Tarantino  and Steven Spielberg)

Showing the songs of a group (or the movies of a director) is not implemented yet, but they can be seen from the django admin interface

If the user is not logged, the navbar shows the "Register" and "Log in" buttons. If the user is logged, the navbar shows the "Logout" and "MyProfile" buttons.

<<<<<<< HEAD
### How to run the application using docker-compose

The user must have the django and docker-compose installed. If not, the user won't be able to run the docker.


First, we must be in the Web-App/MML directory.

Then, we have to migrate the database, using the following command:

  $sudo python3 manage.py migrate

Then, we create a superuser, using the following command:

  $sudo python3 manage.py createsuperuser

and follow the instructions (give a name, password and email for the administrator user)


Finally, for running the application, the following command:

  $sudo docker-compose up


This will run the application.

For visitting the application as a user, write in the browser the url "localhost:8000".
For starting the admin interface, just press the button "Django admin" at the right of the navbar, or go to the url "localhost:8000/admin".

### How to run the application on Heroku
Running on (https://mymedialist.herokuapp.com)

###Superuser
User: admin
Password: admin

