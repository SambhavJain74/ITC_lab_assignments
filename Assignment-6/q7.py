'''Write a Python program to create two empty classes, Student and Marks. Now create
some instances and check whether they are instances of the said classes or not. Also,
check whether the said classes are subclasses of the built-in object class or not.'''

class Student:
    pass

class Marks:
    pass

sambhav=Student()

sambhav_ke_marks=Marks()

print("sambhav is an instance of class Student:",isinstance(sambhav,Student))
print("sambhav is an instance of class Marks:",isinstance(sambhav,Marks))
print("sambhav_ke_marks is an instance of class Student:",isinstance(sambhav_ke_marks,Student))
print("sambhav_ke_marks is an instance of class Marks:",isinstance(sambhav_ke_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))