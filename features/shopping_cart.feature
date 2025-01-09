  Feature: Shopping Cart Functionalities

    Scenario: Shopping Cart page is accessible only when logged in
      Given I am on the login page
      When I try to go to the shopping cart page
      Then I should be redirected to the login page
      And I see error message "Epic sadface: You can only access '/cart.html' when you are logged in."

    Scenario: Cart is empty if user hasn't added items
      Given I am logged in as "standard_user"
      And I am on the products page
      When I click on shopping cart icon
      And I am on shopping cart page
      Then I see shopping cart is empty

    Scenario: Cart has an item when user adds it
      Given I am logged in as "standard_user"
      And I am on the products page
      When I click "Add to the cart" button on "sauce-labs-backpack" item
      And I click on shopping cart icon
      And I am on shopping cart page
      Then I see "Sauce Labs Backpack" item in the cart

      Scenario: Products page UI elements are displayed - empty cart
        Given I am logged in as "standard_user"
        When I click on shopping cart icon
        #Then I see the shopping page title
        And I see the burger menu icon
        And I see the shopping cart icon
        And I see the filter dropdown menu
        And I see "QTY" element
        And I see "Description" element
        And I see "Continue Shopping" element
        And I see "Checkout" element

      Scenario: Products page UI elements are displayed - full cart
        Given I am logged in as "standard_user"
        And I am on the products page
        When I click "Add to the cart" button on "sauce-labs-backpack" item
        And I click on shopping cart icon
        And I am on the shopping cart page
        #Then I see the page title
        And I see the burger menu icon
        And I see the shopping cart icon
        And I see the filter dropdown menu
        And I see "QTY" and "Description" elements
        And I see "Sauce Labs Backpack" item in the cart
        And I see the price for "Sauce Labs Backpack" item
        And I see the description for "Sauce Labs Backpack" item
        And I see "Continue Shopping" button
        And I see "Checkout" button

      Scenario: User can go back and continue shopping
      Scenario: User can delete items from the cart
      Scenario: User can go to checkout from the cart