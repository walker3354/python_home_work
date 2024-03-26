# super() = Function used to give access to the methods of a parent class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calcuate_area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length=length, width=width)


class Cube(Rectangle):
    def __init__(self, length, width, heigth):
        super().__init__(length=length, width=width)
        self.heigth = heigth


square = Square(3, 3)
cube = Cube(4, 4, 4)

print(cube.calcuate_area())
print(square.calcuate_area())
