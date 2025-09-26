
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "dummy" #input("Enter username: ")
password = "dummy123" #input("Enter password: ")
url = "https://www.stealmylogin.com/demo.html"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
input("press enter to close")