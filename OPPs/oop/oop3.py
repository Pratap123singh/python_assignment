#Add attributes and delete attributes from an instance
class student:
    def __init__(self,marks1,marks2):         #instance method
        self.marks1=marks1
        self.marks2=marks2

obj1=student(10,20)
obj2=student(40,50)
obj2.marks3=60
print(obj1.marks1, obj1.marks2)                 #10 20
print(obj2.marks1, obj2.marks2, obj2.marks3)    #40 50 60
del obj2.marks2
print(obj1.marks1, obj1.marks2)                 #10 20
print(obj1.mark1, obj2.mark2)                   #AttributeError: