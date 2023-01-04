import random
for i in range(1,11):
    a=random.randint(1,10)
    b=random.randint(1,10)
    print("Question "+str(i)+":",a,"x",b,"= ")
    c=int(input())
    if c==a*b:
        print("Right!")
    else:
        print("Wrong. The correct answer is", a*b)