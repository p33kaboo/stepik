from selenium import webdriver
import math
import time

driver = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # нахожу элемент по id и узнаю значение атрибута
    driver.get("http://suninjuly.github.io/get_attribute.html")
    img_valuex = driver.find_element_by_id("treasure")
    atribute_img = img_valuex.get_attribute("valuex")

    # записываю значение атрибута в форму на сайте
    get_form = driver.find_element_by_id("answer")
    get_form.send_keys(calc(atribute_img))

    # нажимаю на чекбоксы, радиобаттоны и сабмит

    get_checkbox = driver.find_element_by_id("robotCheckbox").click()
    get_radiobutton = driver.find_element_by_id("robotsRule").click()
    sbmt_button = driver.find_element_by_tag_name("button").click()


finally:
    time.sleep(5)
    driver.quit()
    driver.close()