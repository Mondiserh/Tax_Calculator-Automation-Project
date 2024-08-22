from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

def test_tax_calculator_workflow(driver):
    url = 'https://taxcalculator-production.up.railway.app/'
    
    start_time = time.time()
    
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="CALCULATE     TAX"]'))
        )
        load_time = time.time() - start_time
        print(f"Page load time: {load_time} seconds")
        
        assert load_time < 5, f"Page load time is too long: {load_time} seconds"
        
    except Exception as e:
        pytest.fail(f"Failed to load the page or find the 'CALCULATE TAX' link: {e}")

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        driver.find_element(By.ID, 'age').send_keys('25')
        driver.find_element(By.ID, 'income2').send_keys('500000')
        driver.find_element(By.ID, 'additional').send_keys('50000')
        driver.find_element(By.ID, 'deduction').send_keys('12500')
        time.sleep(5)

        clear_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'clearAll')))
        clear_button.click()
        time.sleep(5)
        
    except Exception as e:
        pytest.fail(f"Failed during form interaction: {e}")

    try:
        driver.find_element(By.ID, 'age').send_keys('25')
        driver.find_element(By.ID, 'income2').send_keys('500000')
        time.sleep(2)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )

        submit_start_time = time.time()

        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", submit_button)
        
    
        result_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'repayment')) 
        )
        

        submit_response_time = time.time() - submit_start_time
        print(f"Form submission response time: {submit_response_time} seconds")
        
        assert submit_response_time < 5, f"Form submission response time is too long: {submit_response_time} seconds"
        
        time.sleep(5)
        
    except Exception as e:
        pytest.fail(f"Failed to submit the form: {e}")
