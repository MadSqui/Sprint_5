import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urls import PageUrls

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(PageUrls.MAIN_PAGE)
    yield driver
    driver.quit()