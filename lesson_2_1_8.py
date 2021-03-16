from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    res = int(num2.text) + int(num1.text)
    print(res)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res))
    btn = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()