from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LOGO_LOCATOR = (By.CSS_SELECTOR,"#a-page .auth-navbar .a-link-nav-icon")
HEADER_LOCATOR = (By.CSS_SELECTOR, "h1.a-spacing-small")
NAME_FIELD_LOCATOR = (By.CSS_SELECTOR,"#ap_customer_name")
EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, "#ap_email")
PASSWORD_FIELD_LOCATOR = (By.CSS_SELECTOR, "#ap,password")
PASSWORD_INFORMATION_LOCATOR = (By.CSS_SELECTOR, "#a-page, .auth-inlined-information-message .a-alert-container .a-alert-content")
REENTER_PASSWORD_FIELD_LOCATOR = (By.CSS_SELECTOR, "#ap_password_check")
CONDITIONS_LINK_LOCATOR = (By.CSS_SELECTOR, "#legalTextRow a[href*='condition of use']")
PRIVACY_LINK_LOCATOR = (By.CSS_SELECTOR, "#legalTextRow a[href*='privacy_notice']")
SIGN_IN_LOCATOR = (By.CSS_SELECTOR, "div.a-row a. a-link-emphasis")

@given('Open Amazon Sign-up page')
def open_google(context):
    context.driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.')

