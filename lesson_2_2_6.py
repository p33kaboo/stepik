# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и
# справиться с ужасным и  огромным футером, который дизайнер
# всё никак не успевает переделать.
# Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Если все сделано правильно и достаточно быстро
# (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с числом. Отправьте полученное число в качестве ответа для
# этого задания.
#
# Для этой задачи вам понадобится использовать метод execute_script,
# чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
from selenium import webdriver
import math, time

# функция с математической формулой для х
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()


try:
    browser.get(link) # открываю ссылку
    x = browser.find_element_by_id("input_value") # нахожу элемент с числом
    browser.find_element_by_id("answer").send_keys(calc(int(x.text))) # сразу передаю аргументом
                                                                      # результат работы функции


    # ниже проматываю страницы до нужных элементов, чтобы по ним можно было с ними работать
    robot_chk=browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_chk)
    robot_chk.click()

    browser.find_element_by_id("robotsRule").click()
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
    browser.close()