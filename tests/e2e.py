from selenium import webdriver
#http://ec2-18-219-20-67.us-east-2.compute.amazonaws.com:8777/

# this function will check the score element in the score website.
#  it will check if number between 0 to 1000 and
# if true value will be true.
def test_scores_service(app_url):
    driver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",executable_path='geckodriver.exe')
    driver.get(app_url)
    x = driver.find_element_by_id("score").text[13:]

    driver.quit()
#    print(type(x))
#    print(len(x))
#    print(x)

    try:
        x = int(x)
#        print(type(x))
        print('scores = ',x)
        if x < 0 or x > 1000:
            return False
        else:
            return True
    except ValueError as e:
        return False


# call test_scores_service with right url. true will exit correctly (exit(0) for sake of CI/CD test.
def main():
    status=test_scores_service('http://ec2-18-219-20-67.us-east-2.compute.amazonaws.com:8777/')
    print(status)
    if status == True:
        exit(0)
    else:
        exit(-1)


if __name__ == '__main__':
    main()
