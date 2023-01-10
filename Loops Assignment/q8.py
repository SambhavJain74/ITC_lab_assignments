list1=[]
for i in range(10):
    t=int(input("Enter integer no."+str(i+1)+":"))
    list1.append(t)
print(list1)

print("The positive numbers in the list are:")
for t in list1:
    if t>0:
        print(t)

print("The negative numbers in the list are:")
for t in list1:
    if t<0:
        print(t)

print("The odd numbers in the list are:")
for t in list1:
    if t%2!=0:
        print(t)

print("The even numbers in the list are:")
for t in list1:
    if t%2==0:
        print(t)

'''no_of_occurences=dict()
def histogram(s):
    global no_of_occurences
    for i in s:
        no_of_occurences[i]=s.count(i)
        s.remove(i)

histogram(list1)
print(no_of_occurences)'''

number_set=[*set(list1)]
for i in number_set:
    print(i,"occurs",list1.count(i),"times")
