import random as r

yes= ["yes", "ye", "ys", "y"]
no = ["no", "nope", "nah", "n"]
guesses = []
number = 0


def get_guess(num):
    print("Hi")


def start_game():
    number = r.randint(1, 50)
    chances = 3
    while chances > 0:
        get_guess(number)
        chances = chances - 1


def main():
    print("Hi! You get three chances to guess the right number")
    k = input("Are you get ready? (y/n) >> ")
    if k.lower() in yes:
        print("Get ready!")
        start_game()
    elif k.lower() in no:
        print("Cya soon!")
    else:
        print("Didn't quite get that, please repeat yourself.")
        main()


main()