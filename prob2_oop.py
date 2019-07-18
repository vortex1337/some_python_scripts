class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi*float(self.radius**2)*float(self.height)

    def surface_area(self):
        return 2 * Cylinder.pi * float(self.radius) *float(self.height) + 2 * Cylinder.pi * float(self.radius**2)
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
