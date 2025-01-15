import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://data.worldbank.org/country")
driver.maximize_window()

#scroll down by pixel verticaslly
driver.execute_script("window.scrollTo(0,500);")
#time.sleep(5)
#scroll down to the specific element
india_element=driver.find_element(By.XPATH,"//a[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();",india_element)
#time.sleep(5)
#scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)