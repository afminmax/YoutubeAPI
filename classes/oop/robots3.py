# Python Classes Part 3


class Person:
    def __init__(self, name, gender, hair, isActive, robotOwned):
        self.name = name
        self.gender = gender
        self.hair = hair
        self.isActive = isActive
        self.robotOwned = robotOwned

    def acting(self):
        self.isActive = True

    def retired(self):
        self.isActive = False


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("Domo arrigato I am Mrs Roboto " +
              self.name + ", I am " + self.color + " and weigh "
              + str(self.weight) + " kilos.")


# Instantiate new robot objects
r1 = Robot('Anne', 'pink', 25)
r2 = Robot('Emma', 'green', 15)

# Instantiate new person objects
p1 = Person('Jenna', 'F', 'Brown', False, False)
p2 = Person('Harrison', 'M', 'Brown', False, False)

# Call their working status - default will be False
print('Person 1 is: ' + str(p1.isActive))
print('Person 2 is: ' + str(p2.isActive))

# Set person 1's status to active
p1.isActive = True
print('Person 1 is now: ' + str(p1.isActive))

# We can also set the robotOwned attribute for person 1 to either
# robot 1 or robot 2, it goes from being "False" to the actual object variable of the robot
p1.robotOwned = r2

# We can then get the name of person 1's robot:
p1.robotOwned.introduce_self()

# We can also see the individual value of person 1's robot:
p1.robotOwned.name
p1.robotOwned.color
p1.robotOwned.weight
