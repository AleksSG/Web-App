Feature: View Songs's Data
In order to see the information of a song,
As a anonymous_user
I want to see the name, group, album, genre, release date and url-info of a song.

Background: An anonymous user can find many songs
  Given Exists an anonymous user
  And Exists information about one song, like "7 rings" registered by "admin"
    | name          | group         | album         | genre          | release date  | url-info      |
    | 7 rings       | Ariana Grande | Thank U, Next | Trap-Pop, R&B  | 18/01/2019    |           |

Scenario: View details for a song like "7 rings"
  Given Exists an anonymous user or a registered user
  When I view the details for song "7 rings"
  Then I'm viewing song details including
    | name          | group         | album         | genre          | release date  | url-info      |
    | 7 rings       | Ariana Grande | Thank U, Next | Trap-Pop, R&B  | 18/01/2019    | ??            |
