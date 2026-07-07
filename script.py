from selenium import webdriver

def test_open_browser():
    driver = webdriver.Chrome(r"D:\chromedriver-win64\chromedriver_win64\chromedriver_win64.exe")
    driver.get("https://www.baidu.com")
    driver.quit()