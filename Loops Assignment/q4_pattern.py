# for i in range(1,6):
#     print("* "*i)
# for i in range(1,5):
#     print("* "*(5-i))     # 1.two non-nested for-loops


# for i in range(1,10):
#     if i<=5:
#         print("* "*i)
#     else:
#         print("* "*(10-i))    # 2.if-else inside for loop


# for i in [1,2,3,4,5,4,3,2,1]:     # 3.using list
#     print("* "*i)


for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print('')
for i in reversed(range(1,5)):      # 4.nested for loops
    for j in range(i):
        print("*",end=" ")
    print('')
