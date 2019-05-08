Feature: Register Song
In order to post a new song,
As a admin
I want to add a song in our application's database.

Background: There is an admin
  Given Exists an admin "admin" with password "admin"

Scenario: Register just song name
  Given I login as admin "admin" with password "password"
  When I register song
    | name        |
    | 7 rings     |
  Then I'm viewing the details page for song by "admin"
    | name        |
    | 7 rings     |
  And There are 1 song

Scenario: Register just song name and group
  Given I login as admin "admin" with password "password"
  When I register song
    | name        | group        |
    | 7 rings     | Ariana Grande|
  Then I'm viewing the details page for song by "admin"
    | name        | group        |
    | 7 rings     | Ariana Grande|
  And There are 1 song

Scenario: Register a song name
  Given I login as admin "admin" with password "password"
  When I register song
    | name        |
    | 7 rings     |
  Then I see that the song is already register
    | name        |
    | 7 rings     |
  And There are 1 song

Scenario: Try to register song but I'm not an admin
  Given I'm a registered or an anonymous user
  When I try to register song
  Then I can not do it because I'm not an admin
And There are 0 songs
