import click
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

## check the guess game & the database
#use like the following to run:  python file.py --ip http://3.84.16.226:5000/gamepicker

@click.command()
@click.option ('--ip',prompt="enter the ip add")

def main(ip):
    click.echo(f"your ip is {ip}")
    url_suffix = ":5000/gamepicker"
    url = "http://%s%s" % (ip, url_suffix)
    try:
        ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                                     executable_path='geckodriver.exe')
        ffdriver.get(url)
        ffdriver.find_element_by_name("level").send_keys("1")
        s2 = Select(ffdriver.find_element_by_id('game'))
        s2.select_by_value('memory')
        ffdriver.find_element_by_class_name("form-style-4").submit()
        time.sleep(3)
        ffdriver.find_element_by_name("memory_form").send_keys("101")
        time.sleep(4)
        ffdriver.find_element_by_class_name("form-style-4").submit()
        ffdriver.quit()
    except:
        print("error")
        exit(1)

    exit(0)

if __name__=='__main__':
    main()
