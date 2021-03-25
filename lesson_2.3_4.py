# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.


import os
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert.accept()

    the_x = browser.find_element_by_id("input_value").text

    form_control = browser.find_element_by_id("answer")
    x = calc(the_x)
    form_control.send_keys(x)

    button = browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    browser.close()
    browser.quit()