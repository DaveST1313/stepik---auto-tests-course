from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = int(x_element.text)
    #y_element = browser.find_element_by_css_selector('[id="num2"]')
    #y = int(y_element.text)
    #z=str(x+y)
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    y=calc(x)
    browser.find_element_by_css_selector('[id="answer"]').send_keys(y)
    browser.find_element_by_css_selector('[id="robotCheckbox"]').click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector('[id="robotsRule"]').click()

    #select = Select(browser.find_element_by_css_selector('[id="dropdown"]'))
    #select.select_by_value(z)
    #browser.find_element_by_tag_name("select").click()
    #rowser.find_element_by_css_selector("[value='z']").click()
    #button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    
	
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()