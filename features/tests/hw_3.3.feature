# Created by apple at 2/10/20
Feature: Test Cart Scenario


  Scenario: Use get empty cart by default
  Given Open Amazon main page
  When Click cart icon
  Then Check cart is empty
