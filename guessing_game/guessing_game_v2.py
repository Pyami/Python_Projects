import random as r

yes = ["yes", "ye", "ys", "y"]
no = ["no", "nope", "nah", "n"]
minimum = 0
maximum = 50


def pick_a_number():
    choosen_number = r.randint(minimum, maximum + 1)
    return choosen_number


def check_guess(nm):
    guess = input("Your guess >> ")
    if guess.isdigit():
        user_guess = int(guess)
        if user_guess > nm:
            print("Too large! Try something lower...")
            check_guess(nm)
        elif user_guess < nm:
            print("Too low! try something a bit higher...")
            check_guess(nm)
        else:
            print("Wooohooo! You got it, time to celebrate!!")
            r = input("Do you want to play again? (y/n) >> ")
            if r.lower() in yes:
                print("Restarting...")
                main()
            elif r.lower() in no:
                print("I hope to see you again soon!")
                exit()
            else:
                print("It was nice meeting you.")
                exit()


def start():
    print("The minimum value is {0} and the maximum is {1}".format(minimum, maximum))
    num = pick_a_number()
    r = input("Are you ready? (y/n) >> ")
    if r.lower() in yes:
        print("Great let's begin!")
        check_guess(num)
    elif r.lower() in no:
        print("well start when you're ready...")
        start()
    else:
        print("I didn't quite get that... but I think we can start!")
        check_guess(num)


def main():
    r = input("Hi, are you ready? (y/n) >> ")
    if r.lower() in yes:
        print("That's great let's start.")
        start()
    elif r.lower() in no:
        print("See ya again soon, when you feel like playing :)")
    else:
        print("I didn't quite get that, do you mind repeating yourself?")
        main()


main()