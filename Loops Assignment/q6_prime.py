n=int(input("Enter the first integer of the range"))
m=int(input("Enter the second integer of the range"))       #taking range inputs
for i in range(n,m+1):
    is_prime=True
    for j in range(2,int((i**0.5)+1)):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)
        