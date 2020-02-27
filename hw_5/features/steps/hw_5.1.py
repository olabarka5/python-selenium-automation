from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLORS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .a-button-list li")
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR,  "#variation_color_name .selection")
ADD_TO_CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#add-to-cart-button")

@given('Open Amazon Firmstrong-Single page' )
def open_bike_page(context):
    context.driver.get('https://www.amazon.com/dp/B005I7TPG0/ref=twister_B07SHLSRBW')
@when('Get all bike colors')
def get_all_bike_colors(context):
    context.bike_colors = context.driver.find_elements(*COLORS_BUTTON_LOCATOR)

@then('Check that every color has description')
def color_has_description(context):
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for bike_color in context.bike_colors:
        bike_color.click()
        print(color_title.text)
        print(bike_color.get_attribute('title'))
        assert color_title.text in bike_color.get_attribute('title'), f"Expected {color_title.text} in {bike_color.get_attribute('title')}"

@then('User can add {need_color} bike to cart')
def add_needed_color_bike_to_cart(context, need_color):
    for bike_color in context.bike_colors:
        if need_color in bike_color.get_attribute('title'):
            bike_color.click()
            sleep (1)
            add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON_LOCATOR)
            add_to_cart_button.click()