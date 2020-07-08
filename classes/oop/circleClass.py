class Circle:

    # class object attribute
    pi = 3.1414

    def __init__(self, radius=1):  # radius has default value of 1
        self.radius = radius

        # 1 - you can also do default attribute calculations
        # 2 - note: the class object attribute is noted instead of self
        # this is actually more clear when looking at the code later to
        # know that this was a class-wide attribute.
        self.area = radius * radius * Circle.pi

    def getCircumference(self):
        return self.pi * Circle.radius * 2


a_circle = Circle(5)
a_circle.getCircumference()
a_circle.area
a_circle.pi
