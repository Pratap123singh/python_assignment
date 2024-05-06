class student:
    course_name="DBDA"
    def __init__(self):
        print("inside init")
        self.course_name="PG-DBDA"
obj=student()
print(obj.course_name)

# o/p:
# inside init
# PG-DBDA

# if class variable and instance variable has same name and if we call a method and that variable is present inside
# that method as instance variable, in this case instance variable will get preferrence over class variable.
