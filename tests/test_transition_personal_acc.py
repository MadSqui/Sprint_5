from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_transition_to_personal_account(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.quit()