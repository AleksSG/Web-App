Feature: Delete Song
In order to delete a song,
As a admin
I want to delete a song of our application's database.

Background: There are registered songs
  Given Exists a admin "admin" with password "password"
  And Exists song registered by "admin"
    | name            | group           | album           |
    | 7 rings         | Ariana Grande   | Sweetener       |

Scenario: An admin deletes a song
  Given I login as admin "admin" with password "password"
  When I delete the song with name "7 rings"
    | name            | group           | album           |
    | 7 rings         | Ariana Grande   | Sweetener       |
  Then I'm viewing the details page for song by "admin"
  And There are 0 songs

Scenario: Try to delete a song but I'm not an admin
  Given I'm not an admin
  When I view the details for song "7 rings"
    | name            | group           | album           |
    | 7 rings         | Ariana Grande   | Sweetener       |
  Then I can not delete it
  And There are 0 songs

Scenario: An admin wants to delete a song but it doesn't exist
  Given I login as admin "admin" with password "password"
  When I want the song with name "7 rings" but the song doesn't exist
  Then I can not delete it
  And There are 0 songs
