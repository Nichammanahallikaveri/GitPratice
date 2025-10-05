from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("kaveri")
driver.find_element(By.CSS_SELECTOR,"input[onclick='displayAlert()']").click()
alert=driver.switch_to.alert
name=alert.text
assert "Hello kaveri," in name
alert.accept() #its
# its dismiss the alert or cancel the alert alert.dismiss()

print("the god will help you no worries ")