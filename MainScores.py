from flask import Flask

app = Flask(__name__)


@app.route('/')


#This file’s purpose is to retrieve the current user score from the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
# this is a web server and you can see the page in a browser ( http://127.0.0.1:8777/ in your computer).
def score_server():
    try:
        score = open("Scores.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:blue">The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8777)

