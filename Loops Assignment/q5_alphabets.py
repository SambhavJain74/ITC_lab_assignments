al="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input("Enter the number of rows you want to print\n"))

for i in range(1,n+1):
    print(i,end=' ')                                         #printing i to verify no. of rows printed
    for j in range(int(((i-1)*i)/2),int((i*(i+1))/2)):
        print(al[j%26],end='')      
    print()