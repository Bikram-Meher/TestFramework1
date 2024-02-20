import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from Utilities.HomePageData import HomePageData


class TestTwo(BaseClass):

    def test_e2e2(self, getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Entering Firstname"+getData["firstname"])
        homePage.enterName().send_keys(getData["firstname"])
        log.info("Entering email"+getData["email"])
        homePage.enterEmail().send_keys(getData["email"])
        log.info("Entering Password"+getData["password"])
        homePage.enterPassword().send_keys(getData["password"])
        log.info("Clicking on checkbox")
        homePage.clickCheckbox().click()
        log.info("Clicking on radiobutton")
        homePage.clickRadioButton().click()

        # static dropdown
        # select.select_by_index(0)
        log.info("selecting gender")
        self.selectOptionByText(homePage.dropDownElement(), getData["gender"])
        homePage.clickSubmitButton().click()
        message = homePage.getMessage().text
        log.info(message)
        assert "Success" in message
        homePage.enterExample().send_keys(getData["exampleTextBox"])
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homePage_Data)
    def getData(self, request):
        return request.param


