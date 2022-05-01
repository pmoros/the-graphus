Feature: Login
    As an user
    I want to login to the system
    In order to use it
    Scenario: Registered
        Given I am registered
        When I try to login
        Then I login
    Scenario: Non registered with valid account
        Given I am not registered
        And I have a valid account
        When I try to login
        Then My account is created
        And I get notified about my account creation
        And I login
    Scenario: Invalid account
        Given I have a valid account
        And I am not registered
        When I try to login
        Then I cannot login
        And I get notified that my account is not valid