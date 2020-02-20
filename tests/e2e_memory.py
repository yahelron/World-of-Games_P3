from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

## check the the flow of the memory game
try:
    ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
    ffdriver.get("http://3.124.186.74:5000/gamepicker")
    ffdriver.find_element_by_name("level").send_keys("1")
    s2=Select(ffdriver.find_element_by_id('game'))
    s2.select_by_value('memory')
    ffdriver.find_element_by_class_name("form-style-4").submit()
    time.sleep(2)
    ffdriver.find_element_by_name("memory_form").send_keys("101")
    time.sleep(1)
    ffdriver.find_element_by_class_name("form-style-4").submit()
    ffdriver.quit()
except:
    print("error")
    exit(1)


exit(0)