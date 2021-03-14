from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input_value = browser.find_element_by_id('input_value')

    # считаем значение для х

    y = calc(input_value.text)

    # записал результат в форму
    input_form = browser.find_element_by_id('answer')
    input_form.send_keys(y)

    chek_box_label = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    chek_box_label.click()

    radiobutton_label = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton_label.click()

    time.sleep(3)

    submit_button = browser.find_element_by_css_selector('button')
    submit_button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()