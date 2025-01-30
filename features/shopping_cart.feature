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


      Scenario: User can go back and continue shopping
        Given I am logged in as "standard_user"
        And I am on the products page
        When I click on shopping cart icon
        And I am on shopping cart page
        Then I click "Continue Shopping" button
        And I am on the products page


      Scenario: User can delete items from the cart
        Given I am logged in as "standard_user"
        And I am on the products page
        When I click "Add to the cart" button on "sauce-labs-backpack" item
        And I click on shopping cart icon
        And I am on shopping cart page
        Then I see "Sauce Labs Backpack" item in the cart
        And I click "Remove" button
        And I see no "Sauce Labs Backpack" item in the cart


      Scenario: User can go to checkout from the cart
        Given I am logged in as "standard_user"
        And I am on the products page
        When I click on shopping cart icon
        And I am on shopping cart page
        Then I click "Checkout" button
        And I am on the checkout1 page


      #Scenario: Products page UI elements are displayed - empty cart
      #Scenario: Products page UI elements are displayed - full cart
