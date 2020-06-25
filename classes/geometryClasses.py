class Line:

    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

    def distance(self):
        return ((self.x_coor[1] - self.x_coor[0])**2 + (self.y_coor[1] - self.y_coor[0])**2)**0.5

    def slope(self):
        return (self.y_coor[1] - self.y_coor[0]) / (self.x_coor[1] - self.x_coor[0])


newline = Line((3, 2), (8, 10))
newline.x_coor
newline.x_coor[1]
newline.x_coor[0]

newline.y_coor
newline.y_coor[1]
newline.y_coor[0]

newline.distance()

newline.slope()
