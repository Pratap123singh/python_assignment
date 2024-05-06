class parent:
    def __init__(self,x,y):
        print("inside parent __init__")
        self.x=x
        self.y=y
    def __add__(self,other):
        print("inside parent add")
       
        if isinstance(other,parent) == True:
            print(type(other))
            print(type(self))
            m = self.x + other.x
            n = self.y + other.y
            return parent(m,n)
        else:
            print(type(other))
            print(type(self))
            m = self.x + other
            n = self.y + other
            return parent(m,n)

    def __radd__(self,other):
        print(type(other))
        print(type(self))
        m = other + self.x
        n = other + self.y
        return parent(m,n)
    
p1=parent(500,50)
# print("----------------------")
# p2=parent(10,100)
# print("***********************")
# p3 = p1 + p2
# # print(p3.x,p3.y)
# print("=======================")
# p4 = p1 + 95
# print(p4.x, p4.y)

p5 = 1 + p1
print(p5.x, p5.y)
