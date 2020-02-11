from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = ( By.XPATH, "//input[@id='helpsearch']")
SEARCH_BUTTON_LOCATOR = ( By.XPATH, "//input[@aria-labelledby='helpSearchSubmit-announce']")
HELP_HEADER = (By.CSS_SELECTOR, ".help-content h1")

@given('Open Amazon help page')
def open_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when ('Input{search_text} to search')
def input_to_search_input(context, search_text):
    help_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    help_search_input.clear()
    help_search_input.send_keys('Cancel order')


@when('Click to search button')
def click_to_search_button(context):
    help_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    help_search_button.click()
    sleep(2)

@then('Cancel order page shows {expected_header_text} text')
def check_text(context, expected_header_text):
    actual_header_text = context.driver.find_element(*HELP_HEADER)
    assert expected_header_text in actual_header_text, f'Expected that {actual_header_text.text} would include {expected_header_text}'





