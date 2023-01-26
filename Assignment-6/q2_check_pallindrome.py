'''Write a Python function that checks whether a passed string is palindrome or not. Note:
A palindrome is a word, phrase, or sequence that reads the same backward as forward,
e.g., madam or nurses run.'''

def check_pallindrome():
    str1=input("Enter the string you want to check for pallindrome\n")
    rev="".join(reversed(str1))                                         #reversing the inputted string
    if str1==rev:                                                       #checking equality
        print("Yes\n")
    else:
        print("No\n")

while True:
    check_pallindrome()