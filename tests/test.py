import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pytest_bdd import given, when, then, scenarios


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    browser = webdriver.Chrome(options, service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()


# ============  Login Page =============

scenarios('login.feature')

@given('the user is on the login page')
def login_page(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

@when('the user enters valid username and password')
def enter_valid_credentials(browser):
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

@when('the user enters invalid username or password')
def enter_invalid_credentials(browser):
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("invalid_user")
    password.send_keys("invalidt_user")
    login_button.click()
    sleep(2)

@then('the user is redirected to the inventory page')
def inventory_page(browser):
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

@then('the user see an error message')
def error_message(browser):
    assert browser.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in browser.page_source

# =================== product sort functionality ==================

scenarios('product_sort.feature')

@given('the user is on the inventory page')
def login_page(browser):
    browser.get('https://www.saucedemo.com/')
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

@when('the user selects Name A to Z option from the product sort')
def select_a_z(browser):
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='az']")
    sort_name.click()

@when('the user selects Name Z to A option from the product sort')
def select_z_a(browser):
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(by=By.XPATH, value="//option[@value='za']")
    sort_name.click()

@when('the user selects Price low to high option from the product sort')
def select_lo_hi(browser):
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='lohi']")
    sort_name.click()

@when('the user selects Price high to low option from the product sort')
def select_hi_lo(browser):
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='hilo']")
    sort_name.click()

@then('the products are sorted alphabetically from A to Z')
def verify_a_z(browser):
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Backpack'
    assert product_names[-1].text == 'Test.allTheThings() T-Shirt (Red)'

@then('the products are sorted alphabetically from Z to A')
def verify_z_a(browser):
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Test.allTheThings() T-Shirt (Red)'
    assert product_names[-1].text == 'Sauce Labs Backpack'

@then('the products are sorted by price from low to high')
def verify_lo_hi(browser):
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Onesie'
    assert product_names[-1].text == 'Sauce Labs Fleece Jacket'

@then('the products are sorted by price from high to low')
def verify_hi_lo(browser):
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Fleece Jacket'
    assert product_names[-1].text == 'Sauce Labs Onesie'

# =================== checkout page ==================

scenarios('checkout.feature')

@given('the user is on the login page')
def login_page(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

@when('User logs in with correct credentials')
def enter_valid_credentials(browser):
    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

@when('the user adds an item to the cart')
def add_to_cart(browser):
    item = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(By.XPATH, "//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    sleep(2)

@when('the user goes to the cart')
def go_to_cart(browser):
    cart_button = browser.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    cart_button.click()
    sleep(2)
    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(By.CLASS_NAME, "inventory_item_price").text


@when('the user clicks on the checkout button')
def checkout(browser):
    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()
    sleep(2)

@when('the user enters valid personal information')
def enter_personal_info(browser):
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(By.CLASS_NAME, "checkout_info").is_displayed()
    firstname = browser.find_element(By.ID, 'first-name')
    lastname = browser.find_element(By.ID, 'last-name')
    postalcode = browser.find_element(By.ID, 'postal-code')
    continue_button = browser.find_element(By.ID, 'continue')
    firstname.send_keys("John")
    lastname.send_keys("Doe")
    postalcode.send_keys("12345")
    continue_button.click()
    sleep(2)

@when('the user enters invalid personal information')
def enter_invalid_personal_info(browser):
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(By.CLASS_NAME, "checkout_info").is_displayed()
    firstname = browser.find_element(By.ID, 'first-name')
    lastname = browser.find_element(By.ID, 'last-name')
    postalcode = browser.find_element(By.ID, 'postal-code')
    firstname.send_keys("")
    lastname.send_keys("Doe")
    postalcode.send_keys("invalid")
    continue_button = browser.find_element(By.ID, 'continue')
    continue_button.click()
    sleep(2)

@when('the user confirms the purchase')
def confirm_purchase(browser):
    assert "Checkout: Overview" in browser.page_source
    assert "Payment Information" in browser.find_element(By.CLASS_NAME, "summary_info_label").text
    confirm_purchase_button = browser.find_element(By.ID, 'finish')
    confirm_purchase_button.click()
    sleep(2)

@then('the user sees a confirmation message')
def confirmation_message(browser):
    assert browser.find_element(By.XPATH, "//div[@class='checkout_complete_container']").is_displayed()
    assert 'Thank you for your order!' in browser.find_element(By.CSS_SELECTOR, 'h2').text

@then('the user sees an error message')
def error_message(browser):
    # assert "Error: First Name is required" in browser.page_source
    assert browser.find_element(By.XPATH, "//div[@class='error-message-container error']").is_displayed()
    assert "Error: First Name is required" in browser.find_element(By.CSS_SELECTOR, "h3").text