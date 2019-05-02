Feature: Create Song's Review
In order to share my opinion about a song,
As a user
I want to register a review with a comment about a song.

Background: There is a registered user
    Given Exists a user "hola" with password "hola"

Scenario: Register just a Good song comment
Given I login as user "user" with password "password"
    When I register comment
      | text        |
      | Good Song!  |
    Then I'm viewing the details page for restaurant by "user"
      | name        |
      | The Tavern  |
    And There are 1 comment
