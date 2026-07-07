from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_open_browser():
    # 使用 webdriver-manager 自动管理驱动
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.baidu.com")
    driver.quit()