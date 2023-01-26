def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

def ncr(n,r):
    return int((fact(n)/(fact(n-r)*fact(r))))

n=int(input("Enter the number of rows of Pascal Triangle you want to print"))

str1=""
for j in range(n+1):
    str1=str1+str(ncr(n,j))+" "
nos=len(str1)

for i in range(0,n+1):
    str1=""
    for j in range(i+1):
        str1=str1+str(ncr(i,j))+" "
    print(" "*int((nos-len(str1))/2),str1)