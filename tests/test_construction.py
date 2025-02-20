from data import VALID_EMAIL, INVALID_EMAIL, VALID_PASSWORD, INVALID_PASSWORD, NAME
from locators import RegisterPageLocators
from urls import PageUrls

def test_transition_to_buns_section(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.BUNS_SECTION).click()
    driver.quit()

def test_transition_to_sauces_section(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
    driver.quit()

def test_transition_to_fillings_section(driver):
    driver.get(PageUrls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()
    driver.quit()