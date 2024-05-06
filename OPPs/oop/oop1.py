class student:
    course_name = "DBDA"            #class variable
    def __init__(self,name,rollno,marks1,marks2):       #method
        self.name=name              #instance variable
        self.rollno=rollno          #instance variable
        self.marks1=marks1          #instance variable
        self.marks2=marks2          #instance variable
        student.institue="IACSD"    #class variable
        print("inside __init__")
    
    def display_info(self):                             #instance method
        print(self.name, self.marks1)
    
    def cal_total_marks(self):                          #instance method
        total = self.marks1 + self.marks2
        print("Total marks: ", total)

    def display_institue(cls):                          #class method
        print(cls.institue)

student_object = student("ram",123,10,20)
student_object.display_info()
student_object.cal_total_marks()
student_object.display_institue()

print(student_object.course_name)
print(student_object.name)
print(student_object.rollno)
print(student_object.marks1)
print(student_object.marks2)
print(student_object.institue)

student_object.name="Shivani"
print(student_object.name)              #update instance variable
student_object.institue="CADC"
print(student_object.institue)          #update class variable

