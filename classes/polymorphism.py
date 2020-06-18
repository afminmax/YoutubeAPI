# Polymorphism - refers to the way in which different object classes can share the same method name
# and then those methods can be called from the same place even though a variety of different objects can be passed in.


class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' sagt woof!'


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' sagt meow!'


snoopy = Dog('snoopy')
print(snoopy.speak())

heathcliff = Cat('heathcliff')
print(heathcliff.speak())


for pet in [snoopy, heathcliff]:
    print(type(pet))
    print(pet.speak())

# OUTPUT: dog is an instance of the DOG class, heathcliff is an instance of the CAT class
# they both have a common method called 'speak'
# the method 'speak' does two things depending on which class it was called from

# <class '__main__.Dog'>
# snoopy sagt woof!
# <class '__main__.Cat'>
# heathcliff sagt meow!
