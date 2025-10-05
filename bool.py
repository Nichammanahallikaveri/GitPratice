from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.implicitly_wait(0.5)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# isDisplayed
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()
assert is_email_visible == True