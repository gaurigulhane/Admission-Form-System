from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:/Users/ASUS/OneDrive/Desktop/student feedback form/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/ASUS/OneDrive/Desktop/student feedback form/index.html")

# Fill form
driver.find_element(By.ID, "name").send_keys("gauri")
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("9876543210")
driver.find_element(By.ID, "department").send_keys("CSE")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.ID, "feedback").send_keys("This is a very useful feedback form for students and works perfectly fine")

# Submit
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
driver.quit()