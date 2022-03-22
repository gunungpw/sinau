import random
import sys

truths_section = [
    "Is it True you still suck your thumb because you think it tastes like chicken?",
    "Is it True that you smell your own farts?",
    "Is it True you eat your boogers?",
]
dares_selection = [
    "I Dare you to eat a Peanut Butter and Mayonnaise Sandwich.",
    "I Dare you to go outside and eat the first bug you find.",
    "I Dare you to confess your darkest secret.",
    "I Dare you to confess who you're crushing on.",
]


def welcome():
    print("Welcome to Truth or Dare… wan't to play? ")
    player_response = input("reply yes or no: ")
    player_response = player_response.lower()
    if player_response == "yes":
        print("Let's begin…")
    else:
        print("Come back when you wan't to have some fun…")
        sys.exit()


def gameplay():
    start_game = input("Last chance to back out or keep going…reply yes to begin: ")
    start_game = start_game.lower()
    if start_game == "yes":
        num_ofplayers = int(input("How many players do we have? "))
    if num_ofplayers > 1:
        print("Decide who will be player 1, and so on… Then let's begin.")
        starting_Player = random.randint(1, num_ofplayers)
        print("Player #:", starting_Player, "is up first.")
    while True:
        start_point = input("Truth or Dare?: ")
        start_point = start_point.lower()
        if start_point == "truth":
            print(random.choice(truths_section))
        elif start_point == "dare":
            print(random.choice(dares_selection))
        else:
            print("Input Error!")
            sys.exit()


welcome()
gameplay()
