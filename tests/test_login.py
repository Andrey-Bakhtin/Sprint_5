import pytest
from locators import Locators
from urls import BASE_URL, REGISTER_PAGE, FORGOT_PASSWORD_PAGE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogin:

    def test_login_via_personal_account_button(self, driver, registered_user):
        """Вход через кнопку «Личный кабинет»"""
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT_US)
        )
        
        driver.find_element(*Locators.EMAIL_INPUT_US).send_keys(registered_user["email"])
        driver.find_element(*Locators.PASSWORD_INPUT_US).send_keys(registered_user["password"])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_login_via_registration_form(self, driver, registered_user):
        """Вход через кнопку в форме регистрации"""
        driver.get(REGISTER_PAGE)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.EMAIL_INPUT_US)
        )
        
        driver.find_element(*Locators.EMAIL_INPUT_US).send_keys(registered_user["email"])
        driver.find_element(*Locators.PASSWORD_INPUT_US).send_keys(registered_user["password"])
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_login_via_forgot_password_form(self, driver, registered_user):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(FORGOT_PASSWORD_PAGE)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_LINK)
        ).click()

        driver.find_element(*Locators.EMAIL_INPUT_US).send_keys(registered_user["email"])
        driver.find_element(*Locators.PASSWORD_INPUT_US).send_keys(registered_user["password"])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_logout_from_personal_account(self, driver, account_user):
        """Выход из личного кабинета"""
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        ).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_HEADER)
        )
