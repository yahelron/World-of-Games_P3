import random
from flask import Flask, jsonify, request
# http://127.0.0.1:5001/parameters?difficulty=3&myguess=3
app = Flask(__name__)

@app.route('/parameters')
def parameters():
    difficulty = str(request.args.get('difficulty'))
    myguess = str(request.args.get('myguess'))
#    print(difficulty,generate_number())
    if myguess == 'Yahel':
        return jsonify(message= ":)"), 401
    else:
        difficulty = int(difficulty)
        myguess = int(myguess)
        result = (compare_results(difficulty=difficulty, myguess=myguess))
        return jsonify(difficulty=difficulty, myguess = myguess, generated_number=result[1],result=result[0] )


def generate_number(difficulty):
    secret_number = (random.randint(1, difficulty))
    print("random is ",secret_number)
    return secret_number


def compare_results(difficulty, myguess):
    random_num = generate_number(difficulty)
    if random_num == myguess:
        print("Your Guessed number (", myguess, ") is correct! ")
        # result = {True:random_num}
        # return result
        return True,random_num
    else:
        print("Computer Generated number ", random_num, "my number ", myguess)
        result = {False: random_num}
        # return result
        return False,random_num

#print(compare_results(difficulty=4,myguess=4))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5001)
