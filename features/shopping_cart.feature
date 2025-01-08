#Epic sadface: You can only access '/cart.html' when you are logged in.
  Feature: Shopping Cart Functionalities
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

