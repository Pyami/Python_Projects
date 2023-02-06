# basic calculations

def calc(n1, n2, sign):
    if sign == '+':
        print(n1 + n2)
    elif sign == '-':
        print(n1 - n2)
    elif sign == '*':
        print(n1 * n2)
    elif sign == '/':
        print(n1 / n2)
    else:
        print(0)
    

def get_val():
    num1 = input("Number: ")
    num2 = input("Number: ")
    sign = input("Operator: ")

    if num1 != "" and num2 !="" and sign != "":
        if num1.isdigit() and num2.isdigit() and sign.isdigit() == False:
            calc(int(num1), int(num2), sign)
        else:
            print("Invalid input")
            get_val()
    else:
        get_val()


get_val()