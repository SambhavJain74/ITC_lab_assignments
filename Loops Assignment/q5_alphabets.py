al="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input("Enter the number of rows you want to print\n"))
al=al*(int((n*(n+1))/52)+1)     #multiplying the string by an integer just large enough to accomodate the number of rows

for i in range(1,n+1):
    l=int(((i-1)*i)/2)
    u=int((i*(i+1))/2)
    print(i,al[l:u])        #printing i to verify no. of rows printed

