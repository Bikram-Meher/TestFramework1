from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    productInCart = (By.CSS_SELECTOR, "h4 a")

    def getProductName(self):
        return self.driver.find_element(*CartPage.productInCart)

    cartCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def clickCartCheckoutButton(self):
        self.driver.find_element(*CartPage.cartCheckoutButton).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage






