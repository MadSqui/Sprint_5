from selenium.webdriver.common.by import By
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
from data import VALID_EMAIL, VALID_PASSWORD
from urls import PageUrls

class TestLogout:
    def test_logout(self, driver):
        driver.get(PageUrls.LOGIN_PAGE)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        assert driver.current_url == PageUrls.LOGIN_PAGE