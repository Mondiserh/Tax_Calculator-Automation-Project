#Test Cases
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
def test_open_url(driver):
    url = 'https://taxcalculator-production.up.railway.app/'
    driver.get(url)
    
    time.sleep(5)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="CALCULATE     TAX"]'))
        )
    except Exception as e:
        pytest.fail(f"Failed to load the page or find the element: {e}")

def test_calculateButton(driver):
   url='https://taxcalculator-production.up.railway.app/'
   driver.get(url)

   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   time.sleep(5)
   try:
      wait = WebDriverWait(driver, 10)
      element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn.px-5.py-3.text-white.mt-3.mt-sm-0')))
      driver.find_element(By.ID, 'age').send_keys('25')
      driver.find_element(By.ID, 'income2').send_keys('500000')
      driver.find_element(By.ID, 'additional').send_keys('50000')
      driver.find_element(By.ID, 'deduction').send_keys('12500')
      time.sleep(5)
      clear_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'clearAll')))
      clear_button.click()
      time.sleep(5)
   except Exception as e:
        pytest.fail(f"Could not Click the button")
def test_calculateTax(driver):
    url='https://taxcalculator-production.up.railway.app/'
    driver.get(url)
    time.sleep(5)
    try:
       wait = WebDriverWait(driver, 10)
       driver.find_element(By.ID, 'age').send_keys('25')
       driver.find_element(By.ID, 'income2').send_keys('500000')
       time.sleep(2)
       submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    
       driver.execute_script("arguments[0].scrollIntoView();", submit_button)
       time.sleep(1)  
       driver.execute_script("arguments[0].click();", submit_button)
       time.sleep(5)
    except Exception as e:
        pytest.fail(f"Could not Click the button")
   