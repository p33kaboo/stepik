
# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом.
# Отправьте полученное число в качестве ответа для этого задания.


import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
path = os.path.abspath(__file__)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Tom")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Sawyer")

    email = browser.find_element_by_name("email")
    email.send_keys("hastalavista@gmail.com")

    file = browser.find_element_by_name("file")
    file.send_keys(path)

    send_button = browser.find_element_by_tag_name("button")
    send_button.click()

finally:
    time.sleep(10)
    browser.close()
    browser.quit()