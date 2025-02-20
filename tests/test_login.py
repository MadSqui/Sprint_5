from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_login_from_main_page(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.LOG_IN_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.quit()

def test_login_from_personal_account_button(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()"
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.quit()

def test_login_from_registration_form(driver):
    driver.get(PageUrls.REGISTRATION_PAGE)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.quit()

def test_login_from_password_restore_page(driver):
    driver.get(PageUrls.LOGIN_PAGE)
    driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
    driver.find_element(*PasswordRestorePage.LOGIN_LINK).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(VALID_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    driver.quit()