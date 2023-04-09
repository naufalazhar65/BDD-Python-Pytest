Feature: Checkout

  Scenario: Successful checkout
    Given the user is on the login page
    When User logs in with correct credentials
    When the user adds an item to the cart
    And the user goes to the cart
    And the user clicks on the checkout button
    And the user enters valid personal information
    # And the user selects a payment method
    And the user confirms the purchase
    Then the user sees a confirmation message

  Scenario: Unsuccessful checkout
    Given the user is on the login page
    When User logs in with correct credentials
    When the user adds an item to the cart
    And the user goes to the cart
    And the user clicks on the checkout button
    And the user enters invalid personal information
    # And the user selects a payment method
    Then the user sees an error message
