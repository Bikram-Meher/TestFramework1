from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service("D:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Shop").click()
products = driver.find_elements(By.CSS_SELECTOR, ".card-title a")

i = -1
for product in products:
    i = i+1
    print(product.text)
    productName = product.text
    if productName == "Nokia Edge":
        driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

driver.find_element(By.XPATH,"//div[@id='navbarResponsive']/ul/li/a").click()
productInCart = driver.find_element(By.CSS_SELECTOR, "h4 a").text
print(productInCart)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText















