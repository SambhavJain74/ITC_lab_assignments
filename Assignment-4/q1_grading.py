marks=int(input("Enter marks"))
print("Your grade is ",end="")
if marks>80:
    print("A")
elif 60<marks<=80:
    print("B")
elif 50<marks<=60:
    print("C")
elif 45<marks<=50:
    print("D")
elif 25<=marks<=45:
    print("E")
elif marks<25:
    print("F")
