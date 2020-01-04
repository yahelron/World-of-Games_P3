import random
from Utils import error_message, screen_cleaner, time_sleep


# return a random number from 1 to 101.
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
def get_list_from_user(difficulty):
    print("After seeing the numbers, enter the numbers you saw,\
     each one separated with Enter. ")
    user_list = []
    for i in range(difficulty):
        try:
            x = int(input("enter "))
            user_list.append(x)
        except ValueError as e:
            error_message()

    return user_list


# check if the user guessed the numbers correctly
def is_list_equal(list_a, list_b):
    print("Your answer", list_b)
    print("Presented numbers", list_a)
    if list_a == list_b:
        # print("winner")
        return True
    else:
        # print("loser")
        return False


# call relevant functions and return True is the user won and False if he lost.
def play(difficulty):
    x = is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))
    return x
