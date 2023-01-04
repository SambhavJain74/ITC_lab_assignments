a=0
def ask_date():
    global a
    a=int(input("Enter Date[1-31]:"))
    if (a<1) or (a>31):
        print("Enter a date from 1-31 only")
        ask_date()

b=0
def ask_month():
    global b
    b=int(input("Enter Month[1-12]:"))
    if (b<1) or (b>12): 
        print("Enter a month from 1 to 12 only")
        ask_month()

c=0
def ask_year(): 
    global c
    c=int(input("Enter Year[1800-2025]:"))
    if (c<1800) or (c>2025):
        print("Enter an year from 1800 to 2025 only")
        ask_year()

ask_date()
ask_month()
ask_year()

if ((c%4==0)and(c%100!=0)) or c%400==0:
    ly=True
else:
    ly=False

if b in [1,3,5,7,8,10,12]:
    monthlength=31
elif b in [4,6,9,11]:
    monthlength=30

if b==2:
    if ly:
        monthlength=29
    else:
        monthlength=28

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