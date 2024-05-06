class parent:
    def __init__(self):
        print("inside parent __init__")
        self.a = 100
    def minus(self,x):
        m = x - 10
        return m
    
class child(parent):
    def __init__(self):
        print("inside child init")
    
    # def minus(self,x,y):
    #     m = x - y
    #     return m
    def minus(self,x):
        parent.__init__(self)
        m = self.a - x
        return m
    
obj=parent()
print(obj.minus(120))
print("----------------------------------------")
# obj1=child()
# print(obj1.minus(200,55))
print("----------------------------------------")
obj2=child()
print(obj2.minus(55))