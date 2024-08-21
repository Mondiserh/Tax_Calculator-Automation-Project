"""
This module contains shared fixtures.
"""
from selenium import webdriver
import pytest


@pytest.fixture
def driver():

  # Initialize the ChromeDriver instance
  driver = webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  driver.implicitly_wait(5)

  # Return the WebDriver instance for the setup
  yield driver

  # Quit the WebDriver instance for the cleanup
  driver.quit()
