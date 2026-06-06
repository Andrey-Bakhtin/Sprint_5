import pytest
from locators import Locators
from urls import BASE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestNavigation:

    def test_navigate_to_personal_account(self, driver, account_user):
        # Переход по клику в «Личный кабинет»
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        ), "/profile" in driver.current_url

    def test_navigate_from_account_to_constructor(self, driver, account_user):
        # Переход из «Личного кабинета» в Конструктор
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        )
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_navigate_from_account_to_constructor_with_link(self, driver, account_user):
        # Переход из «Личного кабинета» в Конструктор по ссылке
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
        )

        driver.find_element(*Locators.LOGO_BUTTON).click()

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_BUTTON)
        ).is_displayed()

    def test_navigate_to_section_buns(self, driver):
        # Переход к разделу «Булки»
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCES_HEADER)
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUNS_TAB)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUNS_HEADER)
        ).is_displayed

    def test_navigate_to_section_sauces(self, driver):
        # Переход к разделу «Соусы»
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCES_HEADER)
        ).is_displayed
       
    def test_navigate_to_section_filling_tabs(self, driver):
        # Переход к разделу «Начинки»
        driver.get(BASE_URL)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.FILLINGS_TAB)
        ).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FILLINGS_HEADER)
        ).is_displayed
