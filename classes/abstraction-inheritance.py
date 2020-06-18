# ABSTRACTION & INHERITANCE

# Abstract classes are never expected to be instantiated, they only serve as base classes
# the ANIMAL class below has a constructor the for name attribute which is unique per instance
# the "speak" method is setup so that a sub-class must provide the functionality


class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            'Subclass must implement this abstract method')


squeakers = Animal('squeakers')
squeakers.speak()

# for these classes to use the name attribute, they must pass the main ANIMAL class as an argument
# when done so, the attribute "name" is grafted onto the DOG or CAT object (inherited??)
# the classes then provide a working "speak" method that is polymorphic (looks the same but does different things)


class Dog(Animal):

    def speak(self):
        return self.name + ' sagt woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' sagt meow!'


fuzz = Dog('fuzz')
fuzz.speak()

isis = Cat('isis')
isis.speak()
