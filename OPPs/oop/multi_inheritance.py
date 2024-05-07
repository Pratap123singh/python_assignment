class A:
    def __init__(self):
        print("inside A init")
        self.a=95

    def increment(self):
        self.a+=10
        print("incremented value is: ", self.a)

class B:
    def __init__(self):
        print("inside B init")
        self.b=25

class C(A,B):
    def __init__(self):
        print("inside C init")
        A.__init__(self)
        B.__init__(self)

    def increment(self):
        self.a+=3
        #print("increment: ", self.a)
        return self.a
obj=C()
#print(obj.a)
#obj.increment()
print(obj.increment())
print(obj.increment())
print(obj.increment())