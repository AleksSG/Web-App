# Web-App

A Group Project which consists in creating the background of a Web using Django.

### Motivation

We are asked to do a project from _Universitat de Lleida_ subject 'Project Web'.

### Application idea

We will make a kind of media database which includes music, movies, etc. using the [iTunes API](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) without affiliating where the user can search content in our D.B. and it will be shown all the information about the result. It is limited to 20 querys per minute.
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

# Considerations for the 1st delivery

### Data model documentation
The entities are defined in the /MML/MediaApp/models.py file.
This entities are: Group, Director, Movie, Song and UserProfileInfo

### General considerations of the application

The user has to press the button "Fill database from iTunes API" for filling the application database with songs, movies, directors and groups. All the content is extracted from the iTunes API.

In this case, we just get the songs from a few groups (Melendi, Els amics de les arts, Ariana Grande, Miley Cyrus, Shawn Mendes, Ed Sheeran and Vicetone). Refering to the movies, we just get the movies from a few directors (Martin Scorsese, Joe Russo, Tim Burton, Quentin Tarantino  and Steven Spielberg)

Showing the songs of a group (or the movies of a director) is not implemented yet, but they can be seen from the django admin interface

If the user is not logged, the navbar shows the "Register" and "Log in" buttons. If the user is logged, the navbar shows the "Logout" and "MyProfile" buttons.

### How to run the application using docker-compose

The user must have the django and docker-compose installed. If not, the user won't be able to run the docker.

First, we must be in the Web-App/MML directory.

Then, we have to migrate the database, using the following command:

  `$sudo python3 manage.py migrate`

Then, we create a superuser, using the following command:

  `$sudo python3 manage.py createsuperuser`

and follow the instructions (give a name, password and email for the administrator user)


Finally, for running the application, the following command:

  `$sudo docker-compose up`

This will run the application.

For visitting the application as a user, write in the browser the url "localhost:8000".
For starting the admin interface, just press the button "Django admin" at the right of the navbar, or go to the url "localhost:8000/admin".

### How to run the application on Heroku
Currently running on https://mymedialist.herokuapp.com

###### Superuser details
User: admin
Password: admin

# Considerations for the 2nd delivery

### Data model documentation
As the main idea is the same for the previous models, we reduced to half them.
Our actual entities are: Group, Song, UserProfileInfo and SongComment

### General considerations of the application

The above functionalities cannot be implemented due to lack of time for the delivery deadline and some of them are too complex and unnecessary (not required).
We reduced the functionalities to the following table, as well as with the corresponding permissions for the CRUD (Create, Read, Update, Delete):

Entities | Create | Read | Update | Delete | Expanation
UserProfileInfo | anonymous_user | superuser (owner), user (owner) | - | user (owner) | Register and access to your profile
Group | superuser | everybody | superuser | superuser | The artist of a song. Only admin can modify data
Song | superuser | everybody | superuser | superuser | The songs. Only admin can modify data
SongComment | user | everybody | user (own) | user (own) | Comment the songs. Admin cannot comment

###### Security
It is checked before an action happens (e.g.: Delete SongComment), if the actual user have the permissions shown above to perform that. In the case of modifying data, each user with admin status (superuser) can execute the operation.

Another important thing, in some URL only superuser can enter (e.g.: manage data URL). It is checked if the user has superuser status.
In other cases, it is checked if a user can access to an URL not owned such as the profile URL of another user.

In any case there are not enough permissions to perform an action, a 403 Forbidden code status is shown.

###### Manage data section (superuser)
As said before, only superusers can access to it.

There are 4 buttons with some JQuery actions where each button displays a form to complete, in order to the admin's desire.

All fields are required by Django's form default and it IS NOT considered to change a field to "non required" if another button is active.
Nevertheless, it is not a logical problem because the "submit" button only applies for the actual form.

- Adding content. There are two ways to perform that.
    1. Manually. User has to insert all the required fields correctly in order to save a new instance of the model.
    2. Autocomplete. When writing the "name" field, the program will execute a JQuery & AJAX script which will query to the iTunes API. After that, when choosing one of the resoults, it will autocomplete all the remaining fields. Important: it would make only 20 querys per minute!
- Modifying content. A future improvement, it is possible to insert a script which filters the "Song" choice form where, a Group is selected, it would only appear Songs with that Group. However, we did not implement that due to the difficulty (communication between Django and JQuery script). In the edit page, the model with its current information is shown. User can modify and save changes or delete this model. Attention:
    1. there are NO confirmation messages!
    2. it is set ON DELETE CASCADE!

#### Comment Song (registered user)
A registered user (never superuser, it will not work) can comment a song which will be shown to all the users (anonymous, registered and superusers) below the song information. Once created a comment, the owner of it can modify it (edit its content or delete it). It is checked only the owner can delete the commit. Warning: there are NO confirmation messages on operations!

###### Behave (test features)
Work in progress...

###### Deployment in heroku
We will deploy on https://mymedialist.herokuapp.com (not yet)

#### Behave (test features)
There are some features done, but we haven't been able to work the tests correctly.

#### Deployment in heroku
The application is deployed in https://mymedialist.herokuapp.com

There is a superuser created (admin) and some comments done in songs (like Heartbeat, by Vicetone)

**Superuser details**
User: admin
Password: admin
