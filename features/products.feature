Feature: Inventory page functionalities

  Scenario: Products page is accessible only when logged in
    Given I am on the login page
    When I try to go to the inventory page
    Then I should be redirected to the login page
    And I see error message "Epic sadface: You can only access '/inventory.html' when you are logged in."

  Scenario: Products page UI elements are displayed
    Given I am logged in as "standard_user"
    And I am on the products page
    Then I see the page title
    And I see the burger menu icon
    And I see the shopping cart icon
    And I see the filter dropdown menu
    And I see a list of items with titles, prices, descriptions, images and "add to cart" buttons


