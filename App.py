import math
from flask import Flask, jsonify, request, render_template, redirect,url_for
#from flask import Flask, render_template, request, redirect, url_for, flash
import urllib.request, json
from Score import add_score
import random
import time
#from MemoryGame import generate_sequence, memorygame, memory2

app = Flask(__name__)
# http://127.0.0.1:5000/guessgame?myguess=19&name=myguess
difficulty = 0
@app.route('/')
def my_form():
    return """<html>
            <head>

             <title>World Of Games</title>
            </head>
            <body>
                <h1><div id="game" style="color:red">World of Games</div></h1>
                <h3><div id="game2" style="color:blue">Hello and welcome to the World of Games(WoG). Here you can find many cool games to play</div></h3>
                <h1><div id="link"> <a href="gamepicker">Start</a></div></h1>
            </body>
            </html>
            """

@app.route('/gamepicker')
def home():
    return render_template('home.html')


@app.route('/your-url', methods=['GET','POST'])
def your_url():
    user_game = request.form.get('game')
    difficulty = request.form['level']
    if user_game == 'memory':
        difficulty = int(difficulty)
        return redirect(url_for('memory2', level=difficulty))
        # return redirect('http://127.0.0.1:5002/memory2?level=%d' % (difficulty))
    else:
        difficulty = int(difficulty)
        return redirect(url_for('guessgame',level=difficulty))


@app.route('/guessgame', methods=['GET','POST'])
def guessgame():
    global difficulty
    difficulty = request.args.get('level')
    if request.method == 'POST':
        user_guess = request.values.get('guess_form')
        print(difficulty)
        x = run_guess_game(user_guess, difficulty)
        points = 0
        if x[1] == "winner":
            points = add_score(difficulty)
            print("your points", points)
            points = str(points)
            return render_template('guess_win.html', difficulty=difficulty, result=x[1], points=points)
        else:
            return render_template('guess_lose.html', difficulty=difficulty, result=x[0])

    return render_template('guess.html', difficulty=difficulty, numbers='')



# call API/service of guess according the chosen difficulty (level).
def run_guess_game(difficulty,user_guess):
    level = int(difficulty)
    guess = int(user_guess)
    print("level=", level, "guess=", guess)
    url = urllib.request.urlopen(
        "http://api:5001/parameters?level=%s&guess=%d" % (level,guess))
    data = json.loads(url.read().decode())  # Decoding a web request
    # Parsing results
    results = data['guess']
    # return results
    computer_generated_number = data['computer_generated_number']
    return [computer_generated_number,results]

@app.route('/about')
def about():
    return '@Yahel'
##########################################################
##########################################################

############# Memory game

#########################################################
#########################################################



# app = Flask(__name__)
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
    myurl = """<center><script>setTimeout(function(){window.location.href="/memory?level=%d"},700);</script>""" % difficulty
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
            return render_template('memory_lose.html', difficulty=difficulty, result=output_numbers)

    return render_template('memory.html', difficulty=difficulty, numbers='')


def generate_sequence(difficulty):
    random_list = []
    for i in range(difficulty):
        random_number = (random.randint(1, 101))
        random_list.append(random_number)
    print(random_list)
    time.sleep(0.7)
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

#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, threaded=True, port=5002)



#########################################################
##########################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=5005)