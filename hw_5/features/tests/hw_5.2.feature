# Created by apple at 2/25/20
Feature: Test count Best Sellers in amazon books

  Scenario: Count Best Sellers in amazon books on page
    Given Open Amazon main page
    When Search fantasy book
    Then Count how much Best Seller badges on page
