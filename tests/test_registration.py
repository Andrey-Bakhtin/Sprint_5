from locators import Locators
from urls import BASE_URL
from helpers import get_user_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestRegistration:

    def test_successful_registration(self, driver):
        """Успешная регистрация пользователя"""
        user_data = get_user_data()
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_HEADER)
        ).is_displayed
        
    def test_registration_with_invalid_password(self, driver):
        """Регистрация с невалидным паролем (менее 6 символов)"""
        user_data = get_user_data()
        invalid_user_data = user_data.copy()
        invalid_user_data["password"] = "12345"

        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        driver.find_element(*Locators.REGISTER_LINK).click()

        driver.find_element(*Locators.NAME_INPUT).send_keys(invalid_user_data["name"])
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_user_data["email"])
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(invalid_user_data["password"])

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR)
        ).is_displayed
       
