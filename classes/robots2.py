# Python Classes Part 2

# In this second iteration, we need to add a constructor

# In python, constructors are made with this format __init__
# This constructor takes three arguments and self
# It is good practice to name the attributes the same as the arguments


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("Domo arrigato I am Mrs Roboto " +
              self.name + ", I am " + self.color + " and weigh "
              + str(self.weight) + " kilos.")


# Now, to create a new robot instance, instantiate the class and feed it the argument values
r1 = Robot('Anne', 'pink', 25)
r2 = Robot('Emma', 'green', 15)

# Last, we call the function action in each of the objects:
r1.introduce_self()
r2.introduce_self()
