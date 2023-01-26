'''Write a Python function to check whether a number is perfect or not. According to
Wikipedia : In number theory, a perfect number is a positive integer that is equal to the
sum of its proper positive divisors, that is, the sum of its positive divisors excluding the
number itself (also known as its aliquot sum). Equivalently, a perfect number is a
number that is half the sum of all of its positive divisors (including itself).'''



def check_perfect(n):                          #defining a function which returns True if n is perfect and False if not
    list1=[]                                   #list of divisors of n, currently empty
    for i in range (1,n):                      #loop runs from 1 to n-1
        if n%i==0:
            list1.append(i)                    #if i divides n, i gets appended to the list
    if n==sum(list1):                          #checking equality of n and its sum of divisors(except n)
        return True
    else:
        return False

num=int(input("Do you want to check a number(0) or print list of perfect numbers(1)\n"))
if num==0:
    while True:
        n=int(input("Enter the integer you want to check\n"))
        if(check_perfect(n)):
            print("The entered number is a perfect number\n")
        else:
            print("The entered number is not a perfect number\n")

elif num==1:
    print("Following are the perfect numbers in increasing order")
    j=1
    while True:
        print(j,"\r",end='')
        if check_perfect(j):
            print(j)
        j+=1

# first 10 perfect numbers:6,28,496,8128,33550336,8589869056,137438691328,
# 2305843008139952128,2658455991569831744654692615953842176