from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("http://www.saucedemo.com")

login = driver.find_element(By.ID, "user-name")
login.click()
login.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.click()
password.send_keys("secret_sauce")

loginButton = driver.find_element(By.ID, "login-button")
loginButton.click()
image = driver.find_element(By.XPATH, '//*[@id="item_0_img_link"]/img')

if image.is_displayed():
    print("Zalogowano poprawnie do systemu")