i=input('''This program checks whether a non-degenerate triangle can be formed from given three 
lengths. Press any key to continue''')
a=int(input("Enter the length of the first side\n"))
b=int(input("Enter the length of the second side\n"))
c=int(input("Enter the length of the third side\n"))
if a+b>c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")