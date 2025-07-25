

from abc import ABC, abstractmethod

class Shapes:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes): 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius **2

class Triangle(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    

class Square(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5



class Pizza(Circle):
    def __init__(self, radius):
        self.radius = radius
     

    



shapes = [Circle(4), Triangle(4), Square(4,5), Pizza(5)]

for shape in shapes:
    print(shape.area())
