#Single Class Inheritance

class Planet:
    def __init__(self):
        print("inside Planet __init__(self)")
        self.shape="ellipsoid"
        self.size=10
    
    def display(self):
        print(f"The shape of planet is {self.shape}.")
    
    def increment_size(self):
        self.size+=1
        print("inside Planet: ", self.size)

class Earth(Planet):
    def __init__(self):
        print("Inside earth __init__")
        Planet.__init__(self)   ##call the __init__ of the base class in order to access base class method, attributes
        self.c=[9,8,8]

    def display(self):
        print("inside display of Earth: ", self.size, self.c)

    def increment_size(self):
        self.size+=5
        print("inside earth: ", self.size)

obj=Earth()
obj.display()
                    #Inside earth __init__
                    #Inside Planet __init__(self)
                    #Inside display of Earth:  10 [9, 8, 8]
obj.increment_size()        #inside earth:  15