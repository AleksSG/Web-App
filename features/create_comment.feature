Feature: Create Song's Review
  In order to share my opinion about a song,
  As a user, not superuser
  I want to register a comment in that song.


  Background: Exists registred user and superuser, and some comments
  Given Exists a user "user" with password "password"
  And Exists a superuser "super" with password "superpass"
  And Exists a song "song" of the group "group"


  Scenario: User writes a comment
  Given User "user" is logged in
  And User is in song "song" page
  And "text" is written in content camp
  When "Add comment" button is clicked
  Then A comment is created for the song "song" by group "group" and content "text"

  Scenario: Superuser writes a comment
  Given Superuser "super" is logged in
  When Superuser is in song "song" page
  Then "Add comment" button is not shown
  Then No comment is created
