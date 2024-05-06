class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #print("inside __init__ of class A")
    
    def __add__(self,other):
        if isinstance(other,A) == True:
            print(f"self: {self}, other: {other}")
            m=self.x + other.x
            n=self.y + other.y
            print("obj1 + obj2")
        else:
            m=self.x + other
            n=self.y + other
            print(f"self2: {self}, other2: {other}")
            print("obj1 + int")
        return A(m,n)
   
    def __radd__(self, other):
        print(f"self1: {self}, other1: {other}")
        j=self.x+other
        k=self.x+other
        print("int + obj")
        return A(j,k)
    
p1 = A(10,20)
p2 = A(20,20)
p3 = p1 + 200
print(p3.x,p3.y)
# p4 = p1 + p2
# print(p4.x, p4.y)
# p5 = 200 + p1
# print(p5.x,p5.y)
