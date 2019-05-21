Feature: Edit Song's Comment
  In order to edit my comment of a song,
  As a user, owner of the comment
  I want to register a comment in that song.

  Background: Exists registred user and superuser, and some comments
  Given Exists a user "user" with password "password"
  And Exists a superuser "super" with password "superpass"
  And Exists a song "song" of the group "group"
  And Exists a comment on song "song" by user "user" with content "text"
  And Exists a comment on song "song2" by user "user" with content "text2"
  And Exists a comment on song "song" by user "user3" with content "text3"

  Scenario: User edits his own comment
  Given User "user" is logged in
  And User is in song "song" page
  When User "user" clicks on "Edit comment" of the comment of "user"
  Then Content camp is shown
  And "Delete comment" button is shown
  And "Save changes" button is shown

  Scenario: User edits a comment that is not his
  Given User "user" is logged in
  And User is in song "song" page
  When User "user" clicks on "Edit comment" of the comment of "user3"
  Then "Not owner of this comment" message is shown

  Scenario: Superuser edits a comment
  Given Superuser "super" is logged in
  And Superuser is in song "song" page
  When Superuser "super" clicks on "Edit comment" of any comment
  Then "Not owner of this comment" message is shown
