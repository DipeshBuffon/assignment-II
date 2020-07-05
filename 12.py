'''Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.'''

s = input("Enter a string to be checked:- ")

def is_palindrom(s):
    rev = s[::-1]
    if s==rev:
        print("{} is palindrome".format(s))
    else:
        print("{} is not palindrome".format(s)

is_palindrom(s)
