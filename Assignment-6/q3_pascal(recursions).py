'''Write a Python function that prints out the first n rows of Pascal's triangle. Note:
Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle:
Each number is the two numbers above it added together'''

list1=[]
list2=[]
def nth_row(n):
    global list1,list2
    if n==1:
        list1=[1]
    elif n==2:
        list1=[1,2,1]
    else:
        nth_row(n-1)
        list2=[1]
        for i in range(len(list1)-1):
            list2.append(list1[i]+list1[i+1])
        list2.append(1)
        list1=list2
    return list1

n=int(input("Enter the number of rows of Pascal Triangle you want to print"))

for i in range(1,n+1):
    print(' '*(n-i),end='')
    nth_row(i)
    for j in list1:
        print(j,end=' ')
    print()