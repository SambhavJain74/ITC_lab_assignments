a=int(input("Enter Date[1-31]:"))
b=int(input("Enter Month[1-12]:"))
c=int(input("Enter Year[1800-2025]:"))
if a>31:
    print("Error input correct date")
    exit()
#seeing if input year is a leap year or no
if (c%4==0):
    leapyear=True
else:
    leapyear=False
#defining month length
if b in [1,3,5,7,8,10,12]:
    monthlength=31
elif b in [4,6,9,11]:
    monthlength=30
if b==2:
    if leapyear:
        monthlength=29
    else:
        monthlength=28

if a>monthlength:
    print("Error please input a correct date")
    exit()
#adding a day
if a<monthlength:
    a=a+1
else:
    a=1
    if b==12:
        b=1
        c=c+1
    else:
        b=b+1

print("The Next date will be",a,"/",b,"/",c)