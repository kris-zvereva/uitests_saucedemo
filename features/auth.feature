Feature: Test Authentication

  Scenario: Test Authentication Correct Credentials
  Given I am on the login page
  When I enter "standard_user" in the "Username" field
  And I enter "secret_sauce" in the "Password" field
  And I press "Login" button
  Then I am on the shop page

