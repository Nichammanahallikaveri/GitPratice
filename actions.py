from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# cursor over the element not perform anything but perform will should end of the every action of the element
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,'#mousehover')).perform()
action.context_click(driver.find_element(By.CSS_SELECTOR,'#mousehover')).perform()
action.double_click(driver.find_element(By.LINK_TEXT,'Top')).click().perform()
#action.drag_and_drop()
#action.click_and_hold()

driver.find_element(By.CSS_SELECTOR,'#opentab').click()
print(driver.title)
window_Opend=driver.window_handles
driver.switch_to.window(window_Opend[1])
tile=driver.find_element(By.XPATH,"//h2[text()='Welcome to QAClick Academy ']").text
print(tile)
driver.close()
driver.switch_to.window(window_Opend[0])
assert 'Practice Page' in driver.find_element(By.XPATH,"//h1[text()='Practice Page']").text


