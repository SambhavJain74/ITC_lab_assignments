import math

def ask_side_lengths():
    global a,b,c,s
    a=float(input("Enter the length of the first side(units)"))
    b=float(input("Enter the length of the second side(units)"))
    c=float(input("Enter the length of the third side(units)"))

    if max(a,b,c)>=a+b+c-max(a,b,c):        #checking generacy of the triangle
        print("Enter side lengths of a valid triangle\n")
        ask_side_lengths()
        

ask_side_lengths()      #calling the function to ask the user to input side lengths

s=(a+b+c)/2     #semi-perimeter
delta=math.sqrt(s*(s-a)*(s-b)*(s-c))    #Heron's Formula for area of triangle

print("The area of the triangle with the inputed sides is "+str(delta)+" unit squares")
