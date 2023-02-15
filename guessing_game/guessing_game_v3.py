import random as r

yes= ["yes", "ye", "ys", "y"]
no = ["no", "nope", "nah", "n"]
guesses = []
number = 0


def get_guess(num):
    guess = int(input("What's your guess: "))
    if guess > num:
        print("Too high... a bit lower maybe...")
    elif guess < num:
        print("Too low... a bit higher maybe...")
    else:
        print("Congratulations! You guessed it.")


def start_game():
    number = r.randint(1, 50)
    chances = 3
    while chances > 0:
        get_guess(number)
        chances = chances - 1
        print(f"You have {chances} left")


def main():
    print("Hi! You get three chances to guess the right number")
    k = input("Are you ready? (y/n) >> ")
    if k.lower() in yes:
        print("Get ready!")
        start_game()
    elif k.lower() in no:
        print("Cya soon!")
    else:
        print("Didn't quite get that, please repeat yourself.")
        main()


main()