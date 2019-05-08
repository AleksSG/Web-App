Feature: Edit Song
In order to edit a song,
As a admin
I want to edit a song of our application's database.

Background: There are registered songs
  Given Exists a admin "admin" with password "password"
  And Exists song registered by "admin"
    | name            | group           | album           |
    | 7 rings         | Ariana Grande   | Sweetener       |

Scenario: Edit song registry album
  Given I login as admin "admin" with password "password"
  When I edit the song with name "7 rings"
    | album         |
    | Thank U, Next |
  Then I'm viewing the details page for song by "admin"
    | name            | group           | album           |
    | 7 rings         | Ariana Grande   | Thank U, Next   |
  And There are 1 songs

Scenario: Try to edit a song but I'm not an admin
  Given I'm not an admin
  When I view the details for song "7 rings"
  Then There is no "edit" link available
