from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_logout(driver):
    driver.get(PageUrls.PERSONAL_ACCOUNT_PAGE)
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    driver.quit()