Feature: Create Song's Review
  In order to share my opinion about a song,
  As a user or a superuser
  I want to register a review with a comment about a song.

  Background: There is a registered user or superuser
    Given Exists a user "usuari" with password "password"
    And Exists a song
      | name        |
      | 7 years     |

  Scenario: Register a comment
    Given I login as user "user" with password "password"
    When I register a comment at the song "7 rings"
      | content        | song     |  user    |
      | Good Song!!!!  | 7 years  |  usuari  |
    Then I'm viewing the details page for song, the previous comments and the user's comment
      | content        | song     |  user    |
      | Good Song!!!!  | 7 years  |  usuari  |
    And There are 1 more comment than before

  Scenario: Try to register review but not logged in
    Given I'm not logged in
    When I register a new review at song "7 rings"
      | text        |
      | Good Song!!  |
    Then I'm redirected to the login form
    And There are 0 more comments than before
