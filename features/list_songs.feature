Feature: List Songs of a Group
In order to see the songs of a group
As a anonymous_user
I want to list all the songs of a group

Background: There are 6 registered songs
  Given Exists a group Ariana Grande
  And Exists songs registered by "admin"
    | song's name     | group          |
    | 7 rings         | Ariana Grande  |
    | Into You        | Ariana Grande  |
    | Breathin        | Ariana Grande  |
    | Problem         | Ariana Grande  |
    | God is a woman  | Ariana Grande  |

Scenario: List the last five
  When I list songs
  Then I'm viewing a list containing
    | song's name     |
    | 7 rings         |
    | Into You        |
    | Breathin        |
    | Problem         |
    | God is a woman  |
  And The list contains 5 songs

Scenario: List the last five
  Given Exists song registered by "admin"
    | name            | group          |
    | Focus           | Ariana Grande  |
  When I list songs
  Then I'm viewing a list containing
    | 7 rings         |
    | Into You        |
    | Breathin        |
    | Problem         |
    | God is a woman  |
    | Focus           |
 And The list contains 5 songs
