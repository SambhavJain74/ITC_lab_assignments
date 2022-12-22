gi=float(input("Enter the gross income\n"))
no_of_dep=int(input("Enter the no of dependents\n"))
if gi>10000:
    ti=gi-10000-(3000*no_of_dep)    #taxable income in USD
    t=ti*0.2    #tax in USD
else:
    t=0     
print("The tax is USD",t,"\n")