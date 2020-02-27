# Created by apple at 2/25/20
Feature: Test scenario for choosing colors in amazon

  Scenario: User can change a product color
    Given Open Amazon Firmstrong-Single page
    When  Get all bike colors
    Then  Check that every color has description
    And   User can add Orange bike to cart