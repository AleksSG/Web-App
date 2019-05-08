Feature: Create User
In order to create a new instance of user,
As a anonymous_user
I want to create a new user with its personal details.

Background: There is a anonymous user
  Given Not exists a user "user" with password "password"

Scenario: Register a user
  Given I'm not registered
  When I want to register
    | name        | bday        | password    |
    |             |             |             |
  Then I'm fill the data
    | name        | bday        | password    |
    | user1       | 04/08/1998  | password1   |
  And Now I'm registered

Scenario: Register a user but already exists
  Given I'm not registered
  When I register restaurant
  Then I'm fill the data
    | name        | bday        | password    |
    | user1       | 04/08/1998  | password1   |
  And I can not register because the user already exists
  And I need to fill the data again but with another user
