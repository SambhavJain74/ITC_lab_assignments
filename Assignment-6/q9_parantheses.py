'''Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid.'''

str1=input("Enter the string of parantheses")
for i in ["(("]:
    if i in str1:
        print("Invalid")
    else:
        print("Valid")
