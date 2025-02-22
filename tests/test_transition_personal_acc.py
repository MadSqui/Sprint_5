import pytest
from selenium.webdriver.common.by import By
from locators import MainPageLocators, ProfilePageLocators
from urls import PageUrls

class TestNavigationPersonal:

    def test_transition_to_personal_account(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_LINK).click()
        assert driver.current_url == PageUrls.LOGIN_PAGE