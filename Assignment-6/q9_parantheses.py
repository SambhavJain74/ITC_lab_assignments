'''Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
but "[)", "({[)]" and "{{{" are invalid.'''

str1=input("Enter the string of parantheses")
list1=list()
for i in str1:
    list1.append(i)

def check_validity(list1):
    while '(' in list1:
        if list[list1.index('(')+1]!=')':
            del list1[list1.index('('):list1.index('(')+2]
            print(list1)
        else:
            return "Invalid"
    if '(' in list1 or ')' in list1:
        return "Invalid"

    while '{' in list1:
        if list[list1.index('{')+1]!='}':
            del list1[list1.index('{'):list1.index('}')+2]
            print(list1)
        else:
            return "Invalid"
    if '{' in list1 or '}' in list1:
        return "Invalid"

    while '[' in list1:
        if list[list1.index('[')+1]!=']':
            del list1[list1.index('['):list1.index('[')+2]
            print(list1)
        else:
            return "Invalid"
    if '[' in list1 or ']' in list1:
        return "Invalid"
    if len(list1)==0:
        return "Valid"
    
print(check_validity(list1))