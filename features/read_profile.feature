Feature: Read Own Profile
  In order to read my personal information
  As a user or a superuser
  I want to see my username, email, birthday and comments

  Background: There is a registered user or superuser
    Given Exists a user "usuari" with password "password"
    And exists a user "comentador" with password "password"
    And exists a song "song" of the group "group"
    And a comment for the "7 rings" song
      | content               | song     |  user    |
      | I like this song bro  | 7 years  |  comentador   |


    Scenario: User "usuari" visit his profile
      When Profile button is pressed
      Then Profile "nou" page is shown


    Scenario: User "comentador" visit his profile
      When Profile button is pressed
      Then Profile "comentador" page is shown with
      | user   | bday          | content               | song     |  user         |
      | nou    | May 10, 1999  | I like this song bro  | 7 years  |  comentador   |


#    Scenario: Try to visit my profile but not logged in
#      Given I'm not logged in
#      Then There is no "Profile" button available
