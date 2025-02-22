import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators
from data import VALID_EMAIL, VALID_PASSWORD
from urls import PageUrls

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.LOG_IN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.current_url == PageUrls.PERSONAL_ACCOUNT_PAGE

    def test_login_from_personal_account_button(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.current_url == PageUrls.PERSONAL_ACCOUNT_PAGE

    def test_login_from_registration_form(self, driver):
        driver.get(PageUrls.REGISTRATION_PAGE)
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.current_url == PageUrls.PERSONAL_ACCOUNT_PAGE

    def test_login_from_password_restore_page(self, driver):
        driver.get(PageUrls.LOGIN_PAGE)
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.current_url == PageUrls.PERSONAL_ACCOUNT_PAGE