import pytest
from selenium import webdriver
from urls import REGISTER_PAGE, LOGIN_PAGE
from helpers import generate_email, generate_password, get_user_data
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    user_data = get_user_data()
    driver.get(REGISTER_PAGE)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.NAME_INPUT)
    )
    driver.find_element(*Locators.NAME_INPUT).send_keys(user_data['name'])
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data['email'])
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data['password'])
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    return user_data

@pytest.fixture
def account_user(driver,registered_user):
    driver.get(LOGIN_PAGE)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.EMAIL_INPUT_US))
    driver.find_element(*Locators.EMAIL_INPUT_US).send_keys(registered_user['email'])
    driver.find_element(*Locators.PASSWORD_INPUT_US).send_keys(registered_user['password'])
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return registered_user
  
