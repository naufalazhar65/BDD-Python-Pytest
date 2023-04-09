Feature: Testing Login Functionality

  Scenario: User logs in with correct credentials
    Given the user is on the login page
    When the user enters valid username and password
    Then the user is redirected to the inventory page

  Scenario: User logs in with incorrect credentials
    Given the user is on the login page
    When the user enters invalid username or password
    Then the user see an error message
