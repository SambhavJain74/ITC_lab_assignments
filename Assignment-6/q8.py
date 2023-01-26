''''Write a Python class to find the three elements that sum to zero from a set of n real
numbers.
Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
Output: [[-10, 2, 8], [-7, -3, 10]]'''

str1=input("Enter the integers separated by a space")
set1=[*set(str1.split(" "))]
for i in set1:
    print(i)
    i=int(i)
    print(i)
print(set1)