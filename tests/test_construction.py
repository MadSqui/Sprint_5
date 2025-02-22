from locators import MainPageLocators
from urls import PageUrls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorSections:
    def test_transition_to_buns_section(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        buns_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        )
        buns_section.click()
        active_buns = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_BUNS)
        )
        assert "tab_tab_type_current" in active_buns.get_attribute("class")

    def test_transition_to_sauces_section(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        sauces_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces_section.click()
        active_sauces = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_SAUCES)
        )
        assert "tab_tab_type_current" in active_sauces.get_attribute("class")

    def test_transition_to_fillings_section(self, driver):
        driver.get(PageUrls.MAIN_PAGE)
        fillings_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        fillings_section.click()
        active_fillings = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_FILLINGS)
        )
        assert "tab_tab_type_current" in active_fillings.get_attribute("class")