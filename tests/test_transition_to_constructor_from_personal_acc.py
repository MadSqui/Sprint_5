import pytest
from selenium.webdriver.common.by import By
from locators import MainPageLocators, ProfilePageLocators
from urls import PageUrls


class TestNavigation:
    def test_transition_to_constructor_from_personal_account_button(self, driver):
        driver.get(PageUrls.PERSONAL_ACCOUNT_PAGE)
        driver.find_element(*ProfilePageLocators.CONSTRUCTOR_LINK).click()
        assert driver.current_url == PageUrls.MAIN_PAGE

    def test_transition_to_constructor_from_personal_account_logo(self, driver):
        driver.get(PageUrls.PERSONAL_ACCOUNT_PAGE)
        driver.find_element(*ProfilePageLocators.LOGO).click()
        assert driver.current_url == PageUrls.MAIN_PAGE