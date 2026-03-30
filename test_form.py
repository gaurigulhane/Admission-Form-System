import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for Jenkins
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # We use Chrome here, make sure you have Chrome installed in your system.
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    # Get the absolute path of the index.html so Selenium can test it locally
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f"file:///{os.path.join(current_dir, 'index.html').replace(chr(92), '/')}"
    driver.get(file_path)
    
    yield driver
    driver.quit()

def test_page_opens_successfully(driver):
    assert "Student Feedback Registration Form" in driver.title

def test_leave_mandatory_fields_blank(driver):
    driver.refresh()
    submit_btn = driver.find_element(By.ID, "submitBtn")
    submit_btn.click()
    
    # Check error messages
    assert driver.find_element(By.ID, "nameError").text == "Student Name should not be empty"
    assert driver.find_element(By.ID, "emailError").text == "Email should not be empty"
    assert driver.find_element(By.ID, "mobileError").text == "Mobile Number should not be empty"

def test_invalid_email_format(driver):
    driver.refresh()
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("invalidemail")
    
    submit_btn = driver.find_element(By.ID, "submitBtn")
    submit_btn.click()
    
    assert driver.find_element(By.ID, "emailError").text == "Email should be in proper format"

def test_invalid_mobile_number(driver):
    driver.refresh()
    mobile_input = driver.find_element(By.ID, "mobile")
    mobile_input.send_keys("12345abcde")
    
    submit_btn = driver.find_element(By.ID, "submitBtn")
    submit_btn.click()
    
    assert driver.find_element(By.ID, "mobileError").text == "Mobile Number should contain valid digits only"

def test_valid_data_and_submission(driver):
    driver.refresh()
    
    driver.find_element(By.ID, "studentName").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "mobile").send_keys("1234567890")
    
    # Dropdown selection works properly
    dept_select = Select(driver.find_element(By.ID, "department"))
    dept_select.select_by_value("Computer Science")
    
    # Gender radio button selection
    driver.find_element(By.ID, "genderMale").click()
    
    # Feedback
    feedback_text = "This is a great form and I am writing exactly ten words."
    driver.find_element(By.ID, "feedback").send_keys(feedback_text)
    
    # Submit 
    driver.find_element(By.ID, "submitBtn").click()
    
    # Wait for success message
    time.sleep(1)
    success_msg = driver.find_element(By.ID, "successMessage")
    assert success_msg.is_displayed()
    assert "Form submitted successfully!" in success_msg.text

def test_reset_button_works_correctly(driver):
    driver.refresh()
    
    name_input = driver.find_element(By.ID, "studentName")
    name_input.send_keys("Jane Doe")
    
    reset_btn = driver.find_element(By.ID, "resetBtn")
    reset_btn.click()
    
    assert name_input.get_attribute("value") == ""
