Feature: Sign up
    How new user
    Want sign up to the platform/system
    To allow access to specific functions

Background: 
    Given I am in chrome browser

@steps
  
  Scenario Outline: Successfully sign up
    Given I am in sign up view
    When Complete sign up form with "<Name>" and "<Lastname>"
    And I click sign up button
    Then Redirect to home view and show welcome message
      """
      Hello
      """
    But First need confirm email

    Examples: 
      | Name | Lastname |
      | John | Doe      |
      | Ane  | Doe      |
