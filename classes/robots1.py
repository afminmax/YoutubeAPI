# Python Classes

# Python Classes Example 1
# A simple class without a constructor


class Robot:
    def introduce_self(self):
        print("Domo arrigato I am Mrs Roboto " +
              self.name + ", I am " + self.color + " and weigh "
              + str(self.weight) + " kilos.")


# Instantiate an instance of Robot by creating a variable and calling the new class
r1 = Robot()

# Assign values to the object using dot extension
# Note that the name assignments must equal their names in the function in the class
r1.name = "Kyler"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Anne"
r2.color = "blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()
