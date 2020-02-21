from selenium import webdriver
import time

## check the guess game & the database
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("http://3.124.186.74:5000/gamepicker")
ffdriver.find_element_by_name("level").send_keys("1")
ffdriver.find_element_by_class_name("form-style-4").submit()
time.sleep(2)
ffdriver.find_element_by_name("guess_form").send_keys("1")
ffdriver.find_element_by_class_name("form-style-4").submit()
time.sleep(2)
try:
    x=ffdriver.find_element_by_id("result").text
    print(x)
    ffdriver.quit()

except:
    print("error")
    ffdriver.quit()
    exit(1)

if x=="You are the winner!!!":
    exit(0)
