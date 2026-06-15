class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def info(self):
        print("Length of rectangle: " + str(self.length))
        print("Width of rectangle: " + str(self.width))
        
    def perimeter(self):
        value = 2*(self.length + self.width)
        return value
    
    def area(self):
        result = self.length * self.width
        return result
    
    def shortened(self):
        newLength = 1/2*(self.length)
        newPerimeter = 2*(newLength + self.width)
        return newPerimeter
    


rectangular = Rectangle(7, 10)
rectangular.info()
print("perimeter is " + str(rectangular.perimeter()))
print("area is " + str(rectangular.area()))
print("perimeter after halving length is " + str(rectangular.shortened()))


