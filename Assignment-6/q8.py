''''Write a Python class to find the three elements that sum to zero from a set of n real
numbers.
Input array: [-25, -10, -7, -3, 2, 4, 8, 10]
Output: [[-10, 2, 8], [-7, -3, 10]]'''

class Sum0:
    def output():
        n=int(input("Enter the number of elements in the input array"))
        list1=[]
        for i in range(n):
            temp=int(input())
            list1.append(temp)
        def find_3_tuples(list1):
            list2=[]
            for i in list1:
                for j in list1:
                    for k in list1:
                        if i+j+k==0:
                            list2.append([i,j,k])
            list3=list(set(tuple(sorted(sub)) for sub in list2))
            list3.remove((0,0,0))
            '''list3=[]
            for i in range(len(list2)):
                if list2[i] not in list3:
                    list3.append(list2[i])'''
            return [(list3)]
        print(find_3_tuples(list1))
    

Sum0.output()
