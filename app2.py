from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = int(x_element.text)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(x))))
    y=calc(x)
    browser.find_element_by_css_selector('[id="answer"]').send_keys(y)
    browser.find_element_by_tag_name("button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()