from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# isEnabled
is_enabled_button = driver.find_element(By.NAME, "button_input").is_enabled()
assert is_enabled_button == True