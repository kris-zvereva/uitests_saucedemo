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

  Scenario: User is able to add an item to the cart
    Given I am logged in as "standard_user"
    And I am on the products page
    When I click "Add to the cart" button on "sauce-labs-backpack" item
    Then I see the shopping cart counter value as "1"
    Then I click on shopping cart icon
    And I am on shopping cart page
    And I see "Sauce Labs Backpack" item in the cart

  Scenario: User is able to delete an item from the cart
    Given I am logged in as "standard_user"
    And I am on the products page
    When I click "Add to the cart" button on "sauce-labs-bike-light" item
    Then I click "Remove" button on "sauce-labs-bike-light" item
    And Shopping cart counter is not displayed
    Then I click on shopping cart icon
    And I am on shopping cart page
    And I see no "Sauce Labs Bike Light" item in the cart

  Scenario: User is able to filter items by name (A-Z)
    Given I am logged in as "standard_user"
    And I am on the products page
    When I select "Name (A to Z)" option in filter dropdown
    Then I see products sorted from A to Z

  Scenario: User is able to filter items by name (Z-A)
    Given I am logged in as "standard_user"
    And I am on the products page
    When I select "Name (Z to A)" option in filter dropdown
    Then I see products sorted from Z to A

  Scenario: User is able to filter items by price (low to high)
    Given I am logged in as "standard_user"
    And I am on the products page
    When I select "Price (low to high)" option in filter dropdown
    Then I see products sorted by price from low to high

  Scenario: User is able to filter items by price (high to low)
    Given I am logged in as "standard_user"
    And I am on the products page
    When I select "Price (high to low)" option in filter dropdown
    Then I see products sorted by price from high to low

