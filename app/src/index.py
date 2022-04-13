import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.CHROME.copy()
    )

    wait = WebDriverWait(driver, 10)
    
    driver.get("https://www.google.com")
    
    driver.find_element(By.NAME, "q").send_keys("selenium" + Keys.RETURN)
    
    first_result = wait.until(
        presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent"))

    driver.quit()
