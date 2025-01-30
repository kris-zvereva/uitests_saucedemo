"""
Feature: Burger menu is accessible from every page
  Scenario: Burger menu is accessible on products page
    Given I am logged in as "standard_user"
    And I am on the products page
    And I see the burger menu icon
    When I click on burger menu icon
    Then I see "All items" option
    And I see "About" option
    And I see "Logout" option
    And I see "Reset app state" option
    """