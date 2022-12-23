string_name=str(input("Enter the string:"))
list1=string_name.split()
list_l=[]
for e in list1:
    lower_e=e.lower()
    list_l.append(lower_e)
set1=set(list_l)
dic={}
for el in set1:
    count=list_l.count(el)
    dic.update({el:count})
dic2={}       
set2={1,2}
set2.clear()  
list2=[]     
if len(list1)==1:
    
    for elements in string_name:
        list2.append(elements)
   
    for el in list2:
        set2.add(el.lower())
    
    string_l=string_name.lower()
    for elem in set2:
        
        dic2.update({elem:string_l.count(elem)})
    
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)

else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic)