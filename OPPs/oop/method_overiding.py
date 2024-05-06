class A:
    def __init__(self):
        print("inside __init__(self) of class A")
        self.a=10
    def display(self):
        print("This is class A' a = ", self.a)
        print("self.a = ", self.a)
    def increment(self):
        self.a+=100
        print("A - incremented value: ", self.a)

class B(A):
    def __init__(self):
        #A.__init__(self)
        print("inside __init__(self) of class B")
        self.b=[9,8,7]
    def display_info(self):
        print("inside display_info of class B")
        print(self.a , self.b)
    def increment(self):
        self.a+=500
        print("inside class B. Incremented by 500. New value is: ", self.a)

class E(A):
    def __init__(self):
        A.__init__(self)
        self.e="extension"
        print("inside __init__ of E")
    def display_info(self):
        print(self.e, self.a)
        print("inside display_info of E")
    def increment(self):
        A.increment(self)
        self.a+=1000
        print("inside increment of class E")
        print(self.a)
obj1=E()
obj1.increment()
