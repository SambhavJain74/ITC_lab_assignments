'''Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the
student name and class.'''

def student_data(student_id,**kwargs):
    print("Student ID is ",student_id)
    if 'student_name' in kwargs:
        print("Student name is ",kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student class is ",kwargs['student_class'])
    print()

student_data(student_id="22106001")
student_data(student_id="22106001", student_name="Sambhav Jain")
student_data(student_id="22106001", student_name="Sambhav Jain", student_class="1st Year")