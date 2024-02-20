import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from PageObjects.ProductPage import ProductPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        homePage = HomePage(self.driver)
        log.info("Clicked on Shop Link")
        productPage = homePage.getShopLink()
        log.info("getting all cart titles")
        products = productPage.getProducts() #driver.find_elements(By.CSS_SELECTOR, ".card-footer button")
        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            log.info(productName)
            if productName == "Nokia Edge":
                productPage.AddToCart()[i].click()

        cartPage = productPage.checkOutButton()
        productInCart = cartPage.getProductName().text
        log.info(productInCart)
        checkoutPage = cartPage.clickCartCheckoutButton()
        checkoutPage.EnterLocation().send_keys("Ind")
        self.verifyLinkPresence("India")
        log.info("Entering country name")
        checkoutPage.selectCountry().click()
        log.info("Clicked on agree button")
        checkoutPage.clickAgreeCheckBox().click()
        checkoutPage.clickPurchaseButton().click()
        successText = checkoutPage.getMessage().text
        log.info("Text received from application")
        assert "Success! Thank you!" in successText



