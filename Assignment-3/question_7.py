def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the integer till where fibonacci sequence is to be printed\n"))
sum=0
for i in range(n):
    sum=sum+fibonacci(i)
    print(fibonacci(i),",",end="")
print("\nThe average of this fibonacci series is",sum/n)
