from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC

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

shop_wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item_4_title_link")))
