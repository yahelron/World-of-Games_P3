import random
import math
from Utils import error_message, screen_cleaner, time_sleep
from flask import Flask, flash, redirect, render_template, \
     request, url_for
import time
#import math
#import urllib.request, json
from Score import add_score
app = Flask(__name__)
output_numbers = [0,0]
difficulty = 0
presented_numbers = 0
@app.route('/memory2', methods=['GET','POST'])
def memory2():
    global output_numbers
    global difficulty
    difficulty = int(request.args.get('level'))
    output_numbers = generate_sequence(difficulty)
    numbers = output_numbers
    myurl = """<script>setTimeout(function(){window.location.href="/memory?level=%d"},700);</script>""" % difficulty
    return '{} {}'.format(numbers, myurl)


@app.route('/memory', methods=['GET','POST'])
def memorygame():
    global difficulty
    difficulty = request.args.get('level')
#    difficulty = 2
    if request.method == 'POST':
        # x=get_list_from_user(difficulty)
        print("numbers", output_numbers)
        x = is_list_equal(output_numbers, get_list_from_user(difficulty))
        points = 0
        if x == "Winner":
            points = add_score(difficulty)
            print("your points", points)
            points = str(points)
            return render_template('memory_win.html', difficulty=difficulty, result=x, points=points)
        else:
            return render_template('memory_lose.html', difficulty=difficulty, result=x)

    return render_template('memory.html', difficulty=difficulty, numbers='')


def generate_sequence(difficulty):
    random_list = []
    for i in range(difficulty):
        random_number = (random.randint(1, 101))
        random_list.append(random_number)
    print(random_list)
    time_sleep(0.7)
    screen_cleaner()
    return random_list


# Will get the numbers from the user (user to put the numbers he saw.
# Will return a list of numbers prompted from the user.
# The list length will be in the size of difficulty.
# def get_list_from_user(difficulty):
#     print("After seeing the numbers, enter the numbers you saw,\
#      each one separated with Enter. ")
#     user_list = []
#     for i in range(difficulty):
#         try:
#             x = int(input("enter "))
#             user_list.append(x)
#         except ValueError as e:
#             error_message()
#
#     return user_list
def get_list_from_user(difficulty):
    try:
        user_list = request.values.get('memory_form')
    except ValueError as e:
        error_message()
    return user_list


# check if the user guessed the numbers correctly
def is_list_equal(list_a, list_b):
    for i in range(0, len(list_a)):
        list_a[i] = str(list_a[i])
    print("Your answer", list_b)
    print("Presented numbers", list_a)
    # convert string (from form) to list
    list_b = list_b.split(",")
    if list_a == list_b:
        # print("winner")
        return 'Winner'
    else:
        # show the numbers that wan
        return list_b


# call relevant functions and return True is the user won and False if he lost.
def play(difficulty):
    x = is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
    return x


#play(4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5002)
