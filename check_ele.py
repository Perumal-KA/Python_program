from selenium import webdriver
from selenium.webdriver.common.by import By

def check_element(url, element_id):
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        element = driver.find_element(By.XPATH, element_id)
        print("Element found!")
    except:
        print("Element not found!")
    finally:
        driver.quit()

# Example usage
check_element("https://www.flipkart.com/", "//span[contains(text(),'Home & Furniture')]")