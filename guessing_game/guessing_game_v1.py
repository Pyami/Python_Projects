import random as r

yes = ["yes", "y", "ye", "ys"]
no = ["no", "nope", "nah", "n"]


def get_limit():
    min = input("What's the Lowest value: ")
    max = input("Whats the maximum value: ")
    if min.isdigit() and max.isdigit():
        take_a_guess(int(min), int(max))
    else:
        print(
            "You gave me the wrong values :<\nCan you give me the correct values... that'll help me by a lot"
        )
        get_limit()


def take_a_guess(min, max):
    if min == max:
        print(
            "Both values are equal... it isn't fun this way... give me other values to work with."
        )
        get_limit()
    elif min > max:
        c = input("Are you sure about this...? ")
        if c.lower() in yes:
            print("Alright, Here I go!!")
            pick_a_number(max, min)
        elif c.lower() in no:
            print("Oh... give me other values in that case")
            get_limit()
        else:
            print("I didn't quite get that... But, let's work with it!")
            pick_a_number(max, min)
    else:
        print("Cool, let's get guessing!")
        pick_a_number(min, max + 1)


def pick_a_number(min, max):
    guess = r.randrange(min, max)

    def check_guess():
        print("My guess is... {0}".format(guess))
        u = input("Is my guess correct? (y/n) >> ")
        if u.lower() in no:
            print("Awww man, I got that wrong...")
            pick_a_number(min, max)
        elif u.lower() in yes:
            print("Hurray! I did it!!")
            inp = input("Thanks for playing with me, would you like to go again? (y/n) >> ")
            if inp.lower() in yes:
                main()
            elif inp.lower() in no:
                print("It was great playing with you!")
                exit()
            else:
                print("See you soon :)")
                exit()
    
    check_guess()


def main():
    ready = input("Hi, are you ready? (y/n) >> ")
    if ready.lower() in yes:
        print("I am ready too! Let's play, but...")
        get_limit()
    elif ready.lower() in no:
        print("It was fun as long as it lasted, Cya again soon :)")
        exit()
    elif ready.lower() not in yes and ready.lower() not in no:
        print("I am sorry I didn't get that... do you mind repeating yourself?")
        main()


main()
