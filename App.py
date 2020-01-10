import math
from flask import Flask, jsonify, request, render_template, redirect,url_for
#from flask import Flask, render_template, request, redirect, url_for, flash
import urllib.request, json
from Score import add_score
app = Flask(__name__)

# http://127.0.0.1:5000/guessgame?myguess=19&name=myguess

@app.route('/')
def my_form():
    return """<html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
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
        return 'memory'
    else:
        return redirect(url_for('guessgame', myguess=6,name=difficulty))



@app.route('/guessgame', methods=['GET','POST'])
def guessgame():
    try:
        name = int(request.args.get('name'))
        myguess = int(request.args.get('myguess'))
        print('name=',name, "myguess=",myguess)
        if request.method == 'POST':
            myguess = request.values.get('guess_form')
            myguess = int(myguess)
            print("forom gusss is:",myguess)
 #           handle_data = '/guessgame?myguess=%s&name=%d' % (myguess,name)
            if math.isnan(myguess):
                myguess = 6
        if myguess < 7:
            result = run_guess_game(myguess, name)
            if result[1] == "winner":
                points=add_score(name)
                print("your points", points)
                points=str(points)
                return render_template('guess.html', difficulty=name, guess=myguess,result=result[1],points=points)
            else:
                return render_template('guess.html', difficulty=name, guess=myguess,result=result[1],points="No new points",win_num="The winner number was %d" % result[0])
        else:
            return "זבל"
    except TypeError:
        return render_template('guess.html', difficulty=5)
    except ValueError:
        return render_template('guess.html', difficulty=5)


    # if myguess < 6:
    #     return render_template('guess.html', difficulty=name, guess=myguess,result=run_guess_game(myguess,name))
    #     #return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    # else:
    #     return jsonify(message="you are not old enough!")

# return render_template('guess.html', difficulty=difficulty, guess1="x=5")



def run_guess_game(level,guess1):
    url = urllib.request.urlopen(
        "http://app:5001/parameters?level=%s&guess=%d" % (level,guess1))
    data = json.loads(url.read().decode())  # Decoding a web request
    # Parsing results
    results = data['guess']
    # return results
    computer_generated_number = data['computer_generated_number']
    return [computer_generated_number,results]


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
