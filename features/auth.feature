Feature: Validating user login functionality

  Scenario: Login succeeds with correct username and password
    Given I am on the login page
    When I enter "standard_user" in the "Username" field
    And I enter "secret_sauce" in the "Password" field
    And I press "Login" button
    Then I am on the products page

  Scenario: Login fails with incorrect username
    Given I am on the login page
    When I enter "wrong_user" in the "Username" field
    And I enter "secret_sauce" in the "Password" field
    And I press "Login" button
    Then I see error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login fails with empty username
    Given I am on the login page
    When I enter "secret_sauce" in the "Password" field
    And I press "Login" button
    Then I see error message "Epic sadface: Username is required"

  Scenario: Login fails with incorrect password
    Given I am on the login page
    When I enter "standard_user" in the "Username" field
    And I enter "super_secret_sauce" in the "Password" field
    And I press "Login" button
    Then I see error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login fails with empty password
    Given I am on the login page
    When I enter "standard_user" in the "Username" field
    And I press "Login" button
    Then I see error message "Epic sadface: Password is required"

  Scenario: Login fails for locked_out user
    Given I am on the login page
    When I enter "locked_out_user" in the "Username" field
    And I enter "secret_sauce" in the "Password" field
    And I press "Login" button
    Then I see error message "Epic sadface: Sorry, this user has been locked out."