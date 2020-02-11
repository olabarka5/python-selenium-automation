from selenium. webdriver. common. by  import By
from  behave  import  given,  when, then
from  time  import  sleep

CART_ICON_LOCATOR = (By.ID, "nav-cart")
CART_HEADER_LOCATOR = (By.CSS_SELECTOR, '#sc-active-cart .sc-empty-cart-header')

@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')


@when('Click cart icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(*CART_ICON_LOCATOR)
    cart_icon.click()
    sleep(2)

@then('Check cart is {expected_cart_header_text}')
def check_cart_header(context, expected_cart_header_text):
    actual_cart_header_text = context.driver.find_element(*CART_HEADER_LOCATOR)
    assert expected_cart_header_text in actual_cart_header_text.text, f'Expected that{actual_cart_header_text.text} would include {expected_cart_header_text}'

