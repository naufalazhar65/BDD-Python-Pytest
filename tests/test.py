import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from pytest_bdd import given, when, then, scenarios

options = Options()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignoare-ssl-errors')
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture
def browser():
    driver = webdriver.Chrome("/Users/naufalazhar/Documents/ChromeDriver/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


# ============  Login Page =============

# scenarios('login.feature')

@given('the user is on the login page')
def login_page(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

@when('the user enters valid username and password')
def enter_valid_credentials(browser):
    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

@when('the user enters invalid username or password')
def enter_invalid_credentials(browser):
    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("invalid_user")
    password.send_keys("invalidt_user")
    login_button.click()
    sleep(2)

@then('the user is redirected to the inventory page')
def inventory_page(browser):
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

@then('the user see an error message')
def error_message(browser):
    assert browser.find_element(by=By.CSS_SELECTOR, value='.error-button').is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in browser.page_source

# =================== checkout page ==================

scenarios('checkout.feature')

@given('the user is on the login page')
def login_page(browser):
    browser.get('https://www.saucedemo.com/')

@when('User logs in with correct credentials')
def enter_valid_credentials(browser):
    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

@when('the user adds an item to the cart')
def add_to_cart(browser):
    item = browser.find_element(by=By.ID, value='add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(by=By.XPATH, value="//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(by=By.CLASS_NAME, value="shopping_cart_badge").text

    sleep(2)

@when('the user goes to the cart')
def go_to_cart(browser):
    cart_button = browser.find_element(by=By.CSS_SELECTOR, value='.shopping_cart_badge')
    cart_button.click()
    sleep(2)
    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(by=By.CLASS_NAME, value="inventory_item_price").text


@when('the user clicks on the checkout button')
def checkout(browser):
    checkout_button = browser.find_element(by=By.ID, value='checkout')
    checkout_button.click()
    sleep(2)

@when('the user enters valid personal information')
def enter_personal_info(browser):
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(by=By.CLASS_NAME, value="checkout_info").is_displayed()
    firstname = browser.find_element(by=By.ID, value='first-name')
    lastname = browser.find_element(by=By.ID, value='last-name')
    postalcode = browser.find_element(by=By.ID, value='postal-code')
    continue_button = browser.find_element(by=By.ID, value='continue')
    firstname.send_keys("John")
    lastname.send_keys("Doe")
    postalcode.send_keys("12345")
    continue_button.click()
    sleep(2)

@when('the user enters invalid personal information')
def enter_invalid_personal_info(browser):
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(by=By.CLASS_NAME, value="checkout_info").is_displayed()
    firstname = browser.find_element(by=By.ID, value='first-name')
    lastname = browser.find_element(by=By.ID, value='last-name')
    postalcode = browser.find_element(by=By.ID, value='postal-code')
    firstname.send_keys("")
    lastname.send_keys("Doe")
    postalcode.send_keys("invalid")
    continue_button = browser.find_element(by=By.ID, value='continue')
    continue_button.click()
    sleep(2)

@when('the user confirms the purchase')
def confirm_purchase(browser):
    assert "Checkout: Overview" in browser.page_source
    assert "Payment Information" in browser.find_element(by=By.CLASS_NAME, value="summary_info_label").text
    confirm_purchase_button = browser.find_element(by=By.ID, value='finish')
    confirm_purchase_button.click()
    sleep(2)

@then('the user sees a confirmation message')
def confirmation_message(browser):
    assert browser.find_element(by=By.XPATH, value="//div[@class='checkout_complete_container']").is_displayed()
    assert 'Thank you for your order!' in browser.find_element(by=By.CSS_SELECTOR, value='h2').text

@then('the user sees an error message')
def error_message(browser):
    # assert "Error: First Name is required" in browser.page_source
    assert browser.find_element(by=By.XPATH, value="//div[@class='error-message-container error']").is_displayed()
    assert "Error: First Name is required" in browser.find_element(by=By.CSS_SELECTOR, value="h3").text