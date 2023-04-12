Feature: Product Sort Functionality

  Scenario: User can sort the products by name (A to Z)
    Given the user is on the inventory page
    When the user selects Name A to Z option from the product sort
    Then the products are sorted alphabetically from A to Z

  Scenario: User can sort the products by name (Z to A)
    Given the user is on the inventory page
    When the user selects Name Z to A option from the product sort
    Then the products are sorted alphabetically from Z to A

  Scenario: User can sort the products by price (low to high)
    Given the user is on the inventory page
    When the user selects Price low to high option from the product sort
    Then the products are sorted by price from low to high

  Scenario: User can sort the products by price (high to low)
    Given the user is on the inventory page
    When the user selects Price high to low option from the product sort
    Then the products are sorted by price from high to low
