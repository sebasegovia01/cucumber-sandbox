Feature: sign in
    Description: allowed to sign in

@steps

  Scenario: Login with credentials
    Given I have account
    When Sign in
    Then Show welcome message
