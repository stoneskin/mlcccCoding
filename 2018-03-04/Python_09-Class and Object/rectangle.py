class Rectangle:
    def __init__(self, width: int= 0, height: int=  0) -> object:
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return  2*(self.width+self.height)
    def printInfo(self):
        print("Rectangle:width="+str(self.width)+";height="+str(self.height))
        print ("Area=", self.getArea())
        print("Perimeter",self.getPerimeter())


