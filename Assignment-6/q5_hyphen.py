'''Write a Python function that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

str1=input("Enter the hyphen-separated sequence of words\n")      #taking the input string
list1=str1.split('-')                                           #extracting the words into a list
list1=sorted(list1)                                             #sorting the words
str1='-'.join(list1)                                            #converting sorted words back to hyphen separated string
print(str1)                                                     #printing the desired string