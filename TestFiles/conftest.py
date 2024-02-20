import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setUp(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        service_obj = Service("D:/Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()







