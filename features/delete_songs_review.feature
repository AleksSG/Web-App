Feature: Delete Song's Review
In order to delete my opinion about a song,
As a user
I want to edit my review about a song.

Background: There is a registered user
  Given Exists a user "hola" with password "hola"
  And Exists song registered by "user"
    | name        |
    | 7 rings     |

Scenario: User deletes a review
  Given Exists review at song "7 rings" by "user"
    | text        |
    | Good Song!  |
  And I login as user "user" with password "password"
  When I delete a review at song "7 rings"
  Then I'm viewing the details page for song by "user"
    | name        |
    | 7 ring      |
  And The list contains 0 review
  And There are 0 comment

Scenario: User try to delete a comment that is not his
  Given Exists review at song "7 rings" by "user1"
    | text        |
    | Good Song!  |
  And I login as user "user2" with password "password"
  When I try to delete a review at song "7 rings" by "user1"
  Then I ("user2") can not edit the review
  And The list contains 1 review
  And There are 1 comment

Scenario: User wants to delete a comment but there is not any review for this song
  Given Doesn't exist review at song "7 rings"
  And I login as user "user" with password "password"
  When I try to delete a review at song "7 rings"
  Then I can not do it
  And The list contains 0 review
  And There are 0 comment
