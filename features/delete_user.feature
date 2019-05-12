Feature: Delete User
  In order to create delete your own user,
  As a user (not a superuser)
  I want to delete my own user from the database.

  Background: Exists registred user and superuser
  Given Exists a user "user" with password "password"
  And Exists a superuser "super" with password "superpass"

  Scenario: User deletes his own user
  Given User "user" is on Profile page
  When "Delete User" button is clicked
  Then User "user" is deleted from database
  And Home page is shown
  And The actual user is an anonymous_user

  Scenario: Superuser delete his own user
  Given Superuser "super" is on Profile page
  Then No "Delete User" button is Showing
  And Superuser "super" is not deleted

  Scenario: anonymous_user deletes another user
  Given anonymous_user in home page
  Then No "Profile" button is shown in navbar
  And No user is deleted
