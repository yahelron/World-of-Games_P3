import random


# Will get a number variable named difficulty
# Will return a random number between 1 to difficulty (the number that the user chosen).
def generate_number(difficulty):
    secret_number = (random.randint(1, difficulty))
    return secret_number


# Will ask the user to guess a number between 1 to difficulty and return the number the user guessed.
def get_guess_from_user(difficulty):
    print("Guess a number between 1 to ", difficulty, end=' ')
    user_guess_num = int(input())
    return user_guess_num


# Will compare the secret generated number to the one prompted by the get_guess_from_user (number the user guessed)
def compare_results(difficulty, secret_number):
    if secret_number == get_guess_from_user(difficulty):
        print("Your Guessed number (", secret_number, ") is correct! ")
        return True
    else:
        print("Computer Generated number ", secret_number)


# call relevant functions and return True is the user won and False if he lost.
def play(difficulty):
    # Will return True / False if the user lost or won.
    x = compare_results(difficulty, generate_number(difficulty))
    if x is True:
        return True
    else:
        return False


