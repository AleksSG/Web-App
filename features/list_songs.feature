Feature: List Songs of a Group
In order to see the songs of a group
As a registred user
I want to list all the songs of a group

Background: There is a registered user
  Given Exists a user "hola" with password "hola"

Scenario: Try to list the songs of a group but user is not logged in
  Given I'm not logged in
  When I list the songs of a group
    | name        |
    | Melendi  |
  Then I'm redirected to the login form
