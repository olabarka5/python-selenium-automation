# Created by apple at 2/10/20
Feature: Find CSS locators

  Scenario: Assert locators on page
    Given Open Amazon Sign-up page
    Then Check logo is a
    Then Check header is h1
    Then Check Name field input
    Then Check Password field input
    Then Check Password information has 6 characters text
    Then Check Reenters Password field input
    Then Check conditions link is a
    Then Check privacy link is a
    Then Check sign-in link is a