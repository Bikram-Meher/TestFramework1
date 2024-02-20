from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    locationTextBox = (By.ID, "country")

    def EnterLocation(self):
        return self.driver.find_element(*CheckOutPage.locationTextBox)

    countryList = (By.LINK_TEXT, "India")

    def selectCountry(self):
        return self.driver.find_element(*CheckOutPage.countryList)

    agreeCheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def clickAgreeCheckBox(self):
        return self.driver.find_element(*CheckOutPage.agreeCheckBox)

    purchaseButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")

    def clickPurchaseButton(self):
        return self.driver.find_element(*CheckOutPage.purchaseButton)

    message = (By.CLASS_NAME, "alert-success")

    def getMessage(self):
        return self.driver.find_element(*CheckOutPage.message)





