#It isnt clear whether question is printing numbers divisible by both 7 and 11 or atleast one, if-conditions for both have been written
for i in range(1,501):
    if i%7==0 or i%11==0:
        print(i)
    #if i%77==0:
       # print(i)
