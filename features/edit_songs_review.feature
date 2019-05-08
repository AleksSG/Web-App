Feature: Edit Song's Review
In order to edit my opinion about a song,
As a registered user
I want to edit my review about a song.

Background: There is a registered user
  Given Exists a user "hola" with password "hola"
  And Exists song registered by "user"
    | name        |
    | 7 rings     |

Scenario: User reviews same song replaces previous review
  Given Exists review at song "7 rings" by "user"
    | text        |
    | Good Song!  |
  And I login as user "user" with password "password"
  When I register a review at song "7 rings"
    | text        |
    | Boring      |
  Then I'm viewing the details page for song by "user"
    | name        |
    | 7 ring      |
  And I'm viewing a song reviews list containing
    | text        | user          |
    | Boring      | user          |
  And The list contains 1 review
  And There are 1 comment

Scenario: User try to edit a comment that is not his
  Given Exists review at song "7 rings" by "user1"
    | text        |
    | Good Song!  |
  And I login as user "user2" with password "password"
  When I try to edit a review at song "7 rings" by "user1"
  Then I ("user2") can not edit the review
  And The list contains 1 review
  And There are 1 comment
