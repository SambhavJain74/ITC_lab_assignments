l_range=int(input("Enter the lower range:\n"))
u_range=int(input("Enter the upper range:\n"))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)