# class animal_kingdom:
#     def __init__(self):
#         print("inside animal_kingdom __init__")
#         self.habbits=['eat', 'sleep', 'defecate', 'wander', 'reproduce']
    
#     def display_animal_kingdom(self):
#         print("animal_kingdom: ",self.habbits)

#     def animal_kingdom_age(self):
#         self.age+=10
#         print("incrmented value animal_kingdom: ", self.age)

# class herbivoures:
#     def __init__(self):
#         print("inside herbivoures init")
#         self.eats="Plants based product"
    
#     def display_herbivoures(self):
#         print("display_herbivoures: ", self.eats)
#         print(self.eats)

#     def herbivoures_age(self):
#         self.age+=20

# class cow(animal_kingdom,herbivoures):
#     def __init__(self):
#         animal_kingdom.__init__(self)   #to access parent class attributes and method
#         herbivoures.__init__(self)      #to access parent class attributes and method

#     def age(self):
#         self.age+=23

# obj=cow()
# print(obj.age())


# class A:
#     def __init__(self):
#         self.a=90               #instance variable

#     def increment(self):
#         self.a += 100
#         print("Incremented value is ", self.a)

# class B:
#     def __init__(self):
#         print("In init of B")
#         self.b="abcd"           #instance variable

#     def new_display(self):
#         print("In class B. b=", self.b)

# class D(A,B):
#     def __init__(self):
#         print("In init of D")
#         A.__init__(self)
#         B.__init__(self)
#         self.d={'k1':'v1'}      #instance variable

#     def display_info(self):
#         print(self.d, self.a)

#     #over ride increment method to add extra functionality!
#     def increment(self):
#         self.a += 500
#         print("In class D, increment by 500. New val is ", self.a)

# d1 = D()
# #print(d1.a, d1.b, d1.d)
# #d1.display()
# #d1.new_display()
# #d1.display_info()
# #d1.increment()

class A:
    def __init__(self):
        self.a=95       
    
    def increment(self):        #instance method
        self.a+=10              #instance variable
        return self.a
    
class B:
    def __init__(self):
        self.b=5

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    
    def increment(self):
        self.a+=3
        return self.a
    
obj=C()
print(obj.increment())
print(obj.increment())
print(obj.increment())
