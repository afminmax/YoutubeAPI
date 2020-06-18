# class inheritance example
class Animal:

    # the first line print statement is a cool way of logging the creation
    # of a new instance of the class
    def __init__(self):
        print('animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('i am eating')


animal1 = Animal()

# class inheritance
# below, i can assign the attributes and methods of the Animal class to
# any new instance of the imaginary Cawawat


class Cawawat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Cawawat imagined!')

    # the method can be overwritten if needed
    def who_am_i(self):
        print('i am a Cawawat! Not just any animal.')

    # additional methods can be added
    def weow(self):
        print("I don't meow like a cat, I meow as weow!")


cawatty = Cawawat()
cawatty.eat()
cawatty.who_am_i()
cawatty.weow()

