word = input("Enter a string: ").lower()

def check(w):
    print("Checking...")
    nw = w[::-1]
    if nw == w:
        print("Palindrome detected!")
    else:
        print("Sorry, this is not a palindrome.")


check(word)