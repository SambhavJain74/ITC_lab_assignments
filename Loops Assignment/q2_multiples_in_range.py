n=int(input("Enter the first number of the range\n"))   
m=int(input("Enter the second number of the range\n"))
t=int(input("Enter the divisor\n"))

print("The numbers in the specified range that are divisible by the divisor are:")
for i in range(n+1,m+1):
    if i%t==0:
        print(str(i)+',',end='')