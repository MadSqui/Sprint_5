from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_transition_to_constructor_from_personal_account_button(self, driver):
    driver.find_element(*MainPageLocators.LOG_IN_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginData.VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()


def test_transition_to_constructor_from_personal_account_logo(self, driver):
    driver.find_element(*MainPageLocators.LOG_IN_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginData.VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginData.VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*ProfilePageLocators.LOGO).click()