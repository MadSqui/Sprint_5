from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_successful_registration(driver):
    driver.get(f"{PageUrls.MAIN_PAGE}/register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

def test_invalid_password_registration(driver):
    driver.get(f"{PageUrls.MAIN_PAGE}/register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    assert "Некорректный пароль" in driver.page_source

