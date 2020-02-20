# Created by apple at 2/12/20
Feature: History books

  Scenario: History books
  Given Open Amazon main page
  When Search history book
  Then Search results counter equal 23
  When If first child price more 10
  Then Add item to cart

