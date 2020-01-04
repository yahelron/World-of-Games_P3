from MemoryGame import play as play_mem
from GuessGame import play
from Utils import error_message, screen_cleaner, time_sleep,  end_game_decision
from Score import add_score
import pymysql


def welcome(name):
    print("Hello ", name, " and welcome to the World of Games(WoG).\nHere you can find many cool games to play.")


"""
 load_game():
 The main function that manage the game.
-  Will get an input from the user about the game he chose – 1/2.  
- After receiving the game number from the user, the function will get the level of difficulty (1-5)
- Will start a new function of the corresponding game with the given difficulty. 
- In case the user won the game, the function will call the function called add_score()  (in score.py module)
to add the new score the user won to the score saved in the Scores.txt function.
In case the user lost, load_game() to load again
 """


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    game_number = input("Choose: 1 or 2: ")
    game_difficulty = 0
    try:
        game_difficulty = int(input("Please choose game difficulty from 1 to 5:  "))
    except ValueError:
        print("You can only put numbers 1-5")
    if game_difficulty < 1 or game_difficulty > 5:
        return error_message()

    if game_number == '1':
        print("Play memory Game")
        # Load the mem game. (MemeoryGame.py --> play(difficulty)
        # i call it play_mem (import play as play_mem) to differentiate between two functions with the same name
        # if the user wan the game, play function to return true.
        if play_mem(game_difficulty) == True:
            add_score(game_difficulty)
            if end_game_decision() == True:
                screen_cleaner()
                load_game()

        else:
            print("You lost this time...")
            time_sleep(7)
            screen_cleaner()
            if end_game_decision()== True:
                screen_cleaner()
                load_game()

    elif game_number == '2':
        print("Play guess Game")
        # will call the guess game (GuessGamy.py --> play(difficulty) ) and check if wan
        if play(game_difficulty) == True:
            add_score(game_difficulty)
            if end_game_decision() == True:
                screen_cleaner()
                load_game()
        else:
            print("You lost this time...")
            time_sleep(4)
            screen_cleaner()
            if end_game_decision()== True:
                screen_cleaner()
                load_game()
    else: # if user entered game number different from 1/2
        print("You can choose only Number 1 or 2")
        return error_message()




#add_score(1)
