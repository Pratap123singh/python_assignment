class A:
    def __init__(self):
        print("inside init of A")
        self.a=90
    
    def increment(self):
        self.a+=100
        print("A: ", self.a)

# class B(A):
#     def __init__(self):
#         print("inside init of B")

#     def increment(self):
#         self.a+=500
#         print("B: ", self.a)

class E(A):
    def __init__(self):
        print("inside init of E")
        A.__init__(self)    
    
    def increment(self):
        A.increment(self)
        self.a+=1000
        print("E: ", self.a)

obj=E()
obj.increment()