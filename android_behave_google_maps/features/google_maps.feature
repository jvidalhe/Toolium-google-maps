Feature: Google Maps Test

  Scenario: Open Google Maps and interact with elements
    Given The Google maps app is open
    When The user skips the initial popup
    Then The search bar is visible
    When The user navigates through the menu items
    Then The user closes the Google Maps app