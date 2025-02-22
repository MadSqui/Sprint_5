from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
from data import VALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from urls import PageUrls

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(PageUrls.REGISTRATION_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PageUrls.LOGIN_PAGE))
        assert driver.current_url == PageUrls.LOGIN_PAGE

    def test_invalid_password_registration(self, driver):
        driver.get(PageUrls.REGISTRATION_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        error_message = driver.find_element(*RegisterPageLocators.INCORRECT_PASSWORD_ERROR).text
        assert error_message == "Некорректный пароль"  in driver.page_source