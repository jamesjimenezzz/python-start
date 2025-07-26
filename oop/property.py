

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self.height = height
    
    @property
    def width(self):
        return f"{self._width:.2f}"
    
    @property
    def height(self):
        return f"{self._height:.2f}"

    @width.setter
    def width(self, new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print(f"Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print(f"Height has been deleted")



rectangle = Rectangle(5, 6)
rectangle.height = 2

del rectangle.width

print(rectangle.height)