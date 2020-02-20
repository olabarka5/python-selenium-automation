from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT_LOCATOR = (By.CSS_SELECTOR, '.nav-search-submit')
SEARCH_RESULTS_LOCATOR = (By.CSS_SELECTOR, '.s-result-list.s-search-results > div[data-index]')
SEARCH_RESULT_PRICE_LOCATOR = (By.CSS_SELECTOR, '.a-price-whole')
SEARCH_RESULT_TITLE_LOCATOR = (By.CSS_SELECTOR, 'h2 a')
ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-button')

@given( 'Open Amazon main page')
def open_google(context):
    context.driver.get('https://www.amazon.com')

@when('Search {search_request}')
def search_text(context, search_request):
    search = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search.clear()
    search.send_keys(search_request)
    search_submit = context.driver.find_element(*SEARCH_SUBMIT_LOCATOR)
    search_submit.click()
    sleep(3)


@then('Search results counter equal {results_counter}')
def count_result(context, results_counter):
    search_results = context.driver.find_elements(*SEARCH_RESULTS_LOCATOR)
    print(len(search_results))
    assert len(search_results) == int(results_counter)

@when('If first child price more {price}')
def check_first_child_price(context, price):
    first_child = context.driver.find_elements(*SEARCH_RESULTS_LOCATOR)[0]
    first_child_price = first_child.find_element(*SEARCH_RESULT_PRICE_LOCATOR)
    context.check_price = int(first_child_price.text) > int(price)

@when('Open good page')
def open_good_page(context):
    if context.check_price:
        first_child = context.driver.find_elements(*SEARCH_RESULTS_LOCATOR)[0]
        first_child_title = first_child.find_element(*SEARCH_RESULT_TITLE_LOCATOR)
        first_child_title.click()
        sleep(3)

@then('Add item to cart')
def add_to_cart(context):
    if context.check_price:
        add_to_cart_button = context.driver.find_element(*ADD_TO_CART_LOCATOR)
        add_to_cart_button.click()
        sleep(3)









