import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver


class Test_001:

  driver = webdriver.Chrome()
  driver.get("https://www.saucedemo.com/")

  def test_login(self):
   self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
   self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
   self.driver.find_element(By.ID,"login-button").click()

   title=self.driver.title
   print(title)

   assert title == "Swag Labs"


  def test_add_to_cart(self):
   self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
   self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
   time.sleep(3)
   self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
   self.driver.find_element(By.ID,"checkout").click()
   time.sleep(5)

   self.driver.find_element(By.ID, "first-name").send_keys("perumal")
   self.driver.find_element(By.ID, "last-name").send_keys("K A")
   self.driver.find_element(By.ID, "postal-code").send_keys("646466")

   self.driver.find_element(By.ID,"continue").click()
   time.sleep(2)

  def finish_payment(self):
   """Complete the payment process."""
   self.driver.find_element(By.ID, "finish").click()
   time.sleep(3)  # Wait to observe the completed payment

  def close_browser(self):
   """Close the browser."""
   self.driver.quit()






