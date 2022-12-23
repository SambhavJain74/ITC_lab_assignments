a=int(input("Enter grade betwwen 4 and 10: "))
if a<4 or a>10:
    print("Entered value is invalid")
else:
    grade=["Outstanding","Excellent",'Very Good','Good','Average','Below Average','Poor']
    performance=['A+','A','B+','B','C+','C','D']
    print('Your grade is',performance[10-a], 'and' , grade[10-a] ,'performance')