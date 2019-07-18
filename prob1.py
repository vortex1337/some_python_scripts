import math
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)

    def slope(self):
        return float(self.coor1[1] - self.coor2[1]) / float(self.coor1[0] - self.coor2[0])
ab=Line((3,2), (8,10))
print(ab.distance())
print(ab.slope())
