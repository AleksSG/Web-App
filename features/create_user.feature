Feature: Create User
  In order to create a new instance of user,
  As a anonymous_user
  I want to create a new user with its personal details.


  Scenario: Register a user "user" with password "password" succesfully
    Given There is not user "user" registred
    When I click Register button
    Then I fill
    And User "user" is registred


  Scenario: Register a user "user" but already exists
    Given Exists a user "user" with password "password"
    When I register a user "user"
    Then I cannot register a new user "user"
