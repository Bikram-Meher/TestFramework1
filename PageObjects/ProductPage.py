from selenium.webdriver.common.by import By

from PageObjects.CartPage import CartPage


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR,".card-title a")

    def getProducts(self):
        return self.driver.find_elements(*ProductPage.products)

    AddProduct = (By.CSS_SELECTOR, ".card-footer button")

    def AddToCart(self):
        return self.driver.find_elements(*ProductPage.AddProduct)

    cartCheckOutbutton = (By.XPATH, "//div[@id='navbarResponsive']/ul/li/a")

    def checkOutButton(self):
        self.driver.find_element(*ProductPage.cartCheckOutbutton).click()
        cartPage = CartPage(self.driver)
        return cartPage

