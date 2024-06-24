import pytest
from selenium import webdriver
from data import TestUrls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(TestUrls.SCOOTER_MAIN_PAGE)
    yield driver
    driver.quit()
