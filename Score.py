import pymysql
import os


"""""""""
- The function will try to read the current score from MySQL DB.
- if it fails it will create a new DB & table and will use it to save the current score.  
 - The function will print the user current score. 
 - Amount of points for winning a game is = 1 point per difficulty level (difficulty 3 = 3 points). 
- Each time the user is winning a game, the points he won will be added to his current amount of point saved in a file.   
- file_name() call the right file to read and write the score (Utils.py)
"""""""""
try:
    conn = pymysql.connect(host='db', port=3306, user='root', passwd='yahelpass', db='sys')
    conn.autocommit(True)
    cursor = conn.cursor()
except pymysql.err.OperationalError as e:
    print(e)

def add_score(difficulty):
    difficulty = int(difficulty)
    try:
        # create DB and tables
        cursor.execute("CREATE DATABASE games;")
        cursor.execute('CREATE TABLE games.users_scores (name varchar(40) NOT NULL, score int NOT NULL) ')
        cursor.execute("INSERT INTO games.users_scores (name, score) VALUES ('game', 0 )")
        # cursor.close()
        # conn.close()
    except Exception:
        pass

    points = read_val()
    points = difficulty + points
    update_points(points)
    print("Congratulations, you've earned ", difficulty, " Points. now you have", points, " points.")
#    cursor.close()
 #   conn.close()
    return points


def read_val():
    cursor.execute("select score from games.users_scores")
    current_points = cursor.fetchone()
#    current_points = cursor.fetchall()
    points = int(current_points[0])
    return points

def update_points(points):
    cursor.execute("UPDATE games.users_scores SET score  = %d  WHERE name = 'game' " % points)



#print(add_score(1))
