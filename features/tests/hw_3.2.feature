# Created by apple at 2/10/20
Feature: Check cancel order page


  Scenario: Verify cancel order page
  Given Open Amazon help page
  When Input cancel order to search
  And Click to search button
  Then Cancel order page shows Cancel Items or Orders text

