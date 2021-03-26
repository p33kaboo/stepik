from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("button").click()

    # переключение между вкладками

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element_by_id("input_value").text
    x = calc(number)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()