import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    yield driver

    driver.quit()