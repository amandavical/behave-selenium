Feature: Testing the DemoQA website

  Scenario: Verify the main page loading
    Given The user accesses the DemoQA main page
    When The page is loaded
    Then The page title should be "DEMOQA"

  Scenario: Verify navigation to the Elements section
    Given The user goes to the DemoQA main page
    When The user clicks on the Elements section
    Then The Elements page should be displayed

  Scenario: Fill and submit the form with valid data
    Given The user accesses the Practice Form
    When The user fills out the form with valid data
    And Clicks submit
    Then A success message should be displayed

  Scenario: Fill and submit the form with invalid data
    Given The user accesses the Practice Form
    When The user fills out the form with invalid data
    And Clicks submit
    Then An error message should be displayed

  Scenario: Attempt to submit the blank form
    Given The user accesses the Practice Form
    When The user tries to submit the blank form
    Then An error message for a blank form should be displayed
