s="Python is a case sensitive language"
print("a. The length of the input string is",len(s))
rev=s[::-1]       #storing the reversed string
print("b.",rev)        #checking reversal of string
new_string=s[10:-9]     #slicing the original string
print("c.",new_string)       #checking sliced string
input_s=s
s=s[:10]+"object oriented"+s[-9:]       #pseudo string mutation
print("d.",s)        #printing the new string
print("e.",input_s.find('a'))
while input_s.find(' ')!=-1:
    input_s=input_s[:input_s.find(' ')]+input_s[input_s.find(' ')+1:]
print("f.",input_s)
