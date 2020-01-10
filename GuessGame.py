import random
from flask import Flask, jsonify, request
# http://127.0.0.1:5001/parameters?level=3&guess=3
app = Flask(__name__)
secret_number_out = 0
user_guess_num = 0
@app.route('/parameters')
def parameters():

    level = int(request.args.get('level'))
    guess = int(request.args.get('guess'))

    global user_guess_num
    user_guess_num = level
    x = play(level)
    x = str(x)
    if guess > 5:
        return jsonify(message= "numbers are too big."), 401
    else:
        return jsonify(level=level, guess = x, computer_generated_number = secret_number_out )


@app.route('/url_variables/<string:level>/<int:guess>')
def url_variables(level: int, guess: int):
    if guess < 18:
        return jsonify(message="Sorry " + level + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + level + ", you are old enough!")


# Will get a number variable named difficulty
# Will return a random number between 1 to difficulty (the number that the user chosen).
def generate_number(difficulty):
    secret_number = (random.randint(1, difficulty))
    return secret_number


# Will ask the user to guess a number between 1 to difficulty and return the number the user guessed.
def get_guess_from_user(difficulty,user_guess_num):
#    print("Guess a number between 1 to ", difficulty, end=' ')
    print("your number is", user_guess_num)
    return user_guess_num


# Will compare the secret generated number to the one prompted by the get_guess_from_user (number the user guessed)
def compare_results(difficulty, secret_number):
    global secret_number_out
    if secret_number == get_guess_from_user(difficulty,user_guess_num):
        print("Your Guessed number (", secret_number, ") is correct! ")
        return True
    else:
        secret_number_out = secret_number
        print("Computer Generated number ", secret_number)


# call relevant functions and return True is the user won and False if he lost.
def play(difficulty):
    # Will return True / False if the user lost or won.
    x = compare_results(difficulty, generate_number(difficulty))
    if x is True:
        return "winner"
    else:
        return "loser"

#user_guess_num = 3
#print(play(5))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5001)
