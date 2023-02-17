num = input("Enter a number: ").lower()

def check(n):
    print("Checking...")
    nn = n[::-1]
    if nn == n:
        print("Palindrome detected!")
    else:
        print("Sorry, this is not a palindrome.")


check(num)