class parent:
    def __init__(self):
        print("inside parent __init__")
        self.a=100
    def display(self):
        print("inside parent display")
        
    def minus(self):
        m = self.a - 10
        return m
    
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("inside child __init__")
    def display_info(self):
        print("inside child display_info")
    def minus(self):
        m = self.a - 5
        return m

obj=parent()
obj.display()
print("----------------------------------------------------------------------")
print(obj.minus())
print("----------------------------------------------------------------------")
obj1=child()
obj1.display_info()
print("----------------------------------------------------------------------")
print(obj1.minus())
