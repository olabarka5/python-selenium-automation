from selenium. webdriver. common. by  import By
from  behave  import  given,  when, then
from  time  import  sleep

CARDS_LOCATOR = (By.CSS_SELECTOR, '#prime-benefit-cards .card-category')

@given('Open Amazon prime page')
def open_google(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(3)


@then('Page will have {benefit_cards} cards')
def search_text(context, benefit_cards):
    given_cards = context.driver.find_elements(*CARDS_LOCATOR)
    assert len(given_cards) == int(benefit_cards), f'Expected_{benefit_cards}, but got {len(given_cards)}'
    sleep(3)