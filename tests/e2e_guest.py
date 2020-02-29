import click
from selenium import webdriver
import time

## check the guess game & the database
#use like the following to run:  python file.py --ip http://3.84.16.226:5000/gamepicker
ip = "192.168.1.30"
url_suffix="gamepicker:5000"
url = "http://%s/%s" % (ip,url_suffix)
print(url)

@click.command()
@click.option ('--ip',prompt="enter the ip add")

def main(ip):
    click.echo(f"your ip is {ip}")
    url_suffix = "gamepicker:5000"
    url = "http://%s/%s" % (ip, url_suffix)
    ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
    ffdriver.get(url)
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


if __name__=='__main__':
    main()
