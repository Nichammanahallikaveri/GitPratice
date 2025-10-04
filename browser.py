from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser="chrome"):
    if browser=="chrome":
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser=="firefox":
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser=="edge":
        return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver = get_driver("edge")  # or "chrome", "firefox"