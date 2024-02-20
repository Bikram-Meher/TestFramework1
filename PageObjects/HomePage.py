from selenium.webdriver.common.by import By

from PageObjects.ProductPage import ProductPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def getShopLink(self):
        self.driver.find_element(*HomePage.shop).click()
        productPage = ProductPage(self.driver)
        return productPage

    NameTextBox = (By.CSS_SELECTOR, "input[name='name']")

    def enterName(self):
        return self.driver.find_element(*HomePage.NameTextBox)

    EmailTextBox = (By.NAME, "email")

    def enterEmail(self):
        return self.driver.find_element(*HomePage.EmailTextBox)

    PasswordTextBox = (By.ID, "exampleInputPassword1")

    def enterPassword(self):
        return self.driver.find_element(*HomePage.PasswordTextBox)

    CheckBox = (By.ID, "exampleCheck1")

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.CheckBox)

    RadioButton = (By.CSS_SELECTOR, "#inlineRadio1")

    def clickRadioButton(self):
        return self.driver.find_element(*HomePage.RadioButton)

    dropDown = (By.ID, "exampleFormControlSelect1")

    def dropDownElement(self):
        return self.driver.find_element(*HomePage.dropDown)

    submitButton = (By.XPATH, "//input[@type='submit']")

    def clickSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    message = (By.CLASS_NAME, "alert-success")

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

    ExampleTextBox = (By.ID, "exampleFormControlSelect1")

    def enterExample(self):
        return self.driver.find_element(*HomePage.ExampleTextBox)






