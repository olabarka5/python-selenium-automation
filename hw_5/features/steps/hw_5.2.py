from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT_LOCATOR = (By.CSS_SELECTOR, '.nav-search-submit')
SEARCH_RESULTS_LOCATOR = (By.CSS_SELECTOR, '.s-result-list. s-search-results > div[data-index]')
SEARCH_RESULTS_BESTSELLER_LOCATOR = (By.CSS_SELECTOR, '.a-badge .a-badge-text')


BESTSELLER_LOCATOR = (By.CSS_SELECTOR, '#a-badge .a-badge-label')

@given( 'Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')

@when("Search {search_request}")
def search_text(context,search_request):
    search=context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search.clear()
    search.send_keys(search_request)
    search_submit = context.driver.find_element(*SEARCH_SUBMIT_LOCATOR)
    search_submit.click()

@then('Count how much {badge_text} badges on page')
def count_result(context, badge_text):
    search_result_badge = context.driver.find_elements(*SEARCH_RESULTS_BESTSELLER_LOCATOR)
    print(len(search_result_badge))


