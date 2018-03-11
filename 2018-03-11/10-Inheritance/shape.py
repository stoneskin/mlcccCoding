# https://www.programiz.com/python-programming/inheritance
class Shape:
    def __init__(self, name: str=""):
        self.name = name

    def printInfo(self):
        print("in shapes, Name=", self.name)

class Polygon(Shape):
    def __init__(self, no_of_sides,name:str="Ploygon"):
        self.name=name;
        Shape.__init__(self, self.name)
    def printInfo(self):
        print("in Ploygon, Name=", self.name)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3,"Triangle")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4,"Rectangle")


print("test")
shape1 = Triangle()
shape1.printInfo()

shape2 = Rectangle()
shape2.printInfo()
