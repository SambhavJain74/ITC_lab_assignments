list1=[]
for i in range(10):
    t=int(input("Enter integer no."+str(i+1)+":"))
    list1.append(t)
print(list1)

for t in list1:
    print("The positive numbers in the list are:")
    if t>0:
        print(t)

for t in list1:
    if t<0:
        print(t)

for t in list1:
    if t%2!=0:
        print(t)

for t in list1:
    if t%2==0:
        print(t)

