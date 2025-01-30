Feature: Checkout page Functionalities
  Scenario: Checkout page is accessible for logged in users
    Given I am on the login page
    When I try to go to the checkout page
    Then I should be redirected to the login page
    And I see error message "Epic sadface: You can only access '/inventory.html' when you are logged in."

  #Scenario: User can enter their info