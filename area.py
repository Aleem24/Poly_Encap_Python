# Making a simple calculator of finding area

# It is for square shope or polygon

class Polygon(object):
    def __init__(self,sideNumber,):
        self.sideNumber = sideNumber
        


    def area(self, sidelength):
        return self.sideNumber * sidelength
    
square = Polygon(20)

print(square.area(4))

