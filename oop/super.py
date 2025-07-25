
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and it is {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def define_color(self):
        print(f"The color of this circle is color {self.color}")
        

    #METHOD OVERWRITING EXAMPLE AND HOW TO USE THE SAME DEFINE IN THE INHERITANCE.

    def describe(self):
        print(f"The width of this radius is {self.radius}cm")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def att(self):
        print(f"The color of this square is color {self.color}. The filled boolean is {self.is_filled}, and the width is {self.width}")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height



circle = Circle("Red", True, 250)
square = Square("Blue", False, 5)

circle.describe()