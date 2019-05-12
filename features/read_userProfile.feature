Feature: Read User Profile
  In order to read your own profile,
  As a owner user or superuser
  I want to read my username, email, birthday and comments.

  Background: Exists registred user and superuser, and some comments
  Given Exists a user "user" with password "password"
  And Exists a user "user2" with password "password"
  And Exists a superuser "super" with password "superpass"
  And Exists a comment on song "song" by user "user" with content "text"
  And Exists a comment on song "song2" by user "user" with content "text2"
  And Exists a comment on song "song" by user "user2" with content "text3"


  Scenario: User "user" reads his own profile
  Given User "user" is logged in
  When "Profile" button is clicked
  Then User "user" personal data is shown
  And Comment on song "song" by user "user" with content "text" is shown
  And comment on song "song2" by user "user" with content "text2" is shown

  Scenario: User "user2" reads his own profile
  Given User "user2" is logged in
  When "Profile" button is clicked
  Then User "user2" personal data is shown
  And Comment on song "song" by user "user2" with content "text3" is shown

  Scenario: Superuser "super" reads his own profile
  Given Superuser "user" is logged in
  When "Profile" button is clicked
  Then User "user" personal data is shown
  And No comments are shown
