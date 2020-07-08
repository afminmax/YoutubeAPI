class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # tuple unpacking
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


newline = Line((3, 2), (8, 10))
newline.x_coor
newline.x_coor[1]
newline.x_coor[0]

newline.y_coor
newline.y_coor[1]
newline.y_coor[0]

newline.distance()

newline.slope()


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.141 * self.radius**2 * self.height

    def surface_area(self):
        return 2 * 3.141 * self.radius * (self.height + self.radius)


newcyl = Cylinder(2, 3)
newcyl.volume()
newcyl.surface_area()
