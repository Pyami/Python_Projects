# Txt based adventure game
player = "Player"

adventures = ["1. Men asking for shelter", "2. A mysterious city", "3. The Legend"]


def list():
    for adv in adventures:
        print(adv)

    selection = input(">> ")


def select_story(choice):
    print("Great Choice!")


def greet(username):
    if username == "":
        player = player
    else:
        player = username
        print("Nice to meet you {0}!\nPlease select a storyline".format(player))
        list()


# main fnuction
def main():
    print("HELLO AND WELCOME... May I get your name?")
    user = input(">> ")
    greet(user)


main()
