A=(input("Enter the first number"))
B=(input("Enter the second number"))
C=(input("Enter the third number"))
a=float(A)
b=float(B)
c=float(C)
if a>=b and a>=c and a!=b!=c:
    print(A,"is the greatest number")
elif b>=a and b>=c and b!=c!=a:
    print(B,"is the greatest number")
elif c>=a and c>=b and c!=a!=b:
    print(C,"is the greatest number")
else:
    print("All three are equal to",A)

