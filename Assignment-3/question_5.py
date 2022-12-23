s="ABCDEFGHIJK"
for i in range(int((len(s)+1)/2)):
    print(" "*i+s)
    s=s[:-2]
