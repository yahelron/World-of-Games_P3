import time
import os
import sys


# general global error message
def error_message():
    print("ERROR_MESSAGE: Something went wrong..")


# clear the screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


# When the a game ends, user to choose if to exit or continue to play (called from load_game() )
def end_game_decision():
    print("Press 'E' to exit or 'P' to play again ")
    exit_or_play = 'A'
    while exit_or_play is not 'E' or exit_or_play is not 'P':
        exit_or_play = input("E/P ")
        if exit_or_play == 'E':
            sys.exit()
        elif exit_or_play == 'P':
            return True


def time_sleep(sec):
    time.sleep(sec)




