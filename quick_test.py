from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_open_browser():
    service = Service(r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.baidu.com")
    print(driver.title)
    driver.quit()