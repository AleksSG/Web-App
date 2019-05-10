Feature: Create Song's Review
In order to share my opinion about a song,
As a user
I want to register a review with a comment about a song.

Background: There is a registered user
  Given Exists a user "hola" with password "hola2222"

Scenario: Register just a good song comment
  Given I login as user "user" with password "password"
  When I register comment
    | text        |
    | Good Song!  |
  Then I'm viewing the details page for song by "user"
    | name        |
    | 7 rings     |
  And There are 1 comment

Scenario: Try to register review but not logged in
  Given I'm not logged in
  When I register a new review at song "7 rings"
    | text        |
    | Good Song!  |
  Then I'm redirected to the login form
  And There 0 comments
