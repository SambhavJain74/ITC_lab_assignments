gi=int(input("Enter the gross income"))
no_of_dep=int(input("Enter the no of dependents"))
ti=gi-10000-3000*no_of_dep
t=ti*0.2
print("the tax is USD ", t)