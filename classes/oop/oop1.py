class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print('meow')

    def get_age(self):
        print(self.age)

    def get_name(self):
        print(self.name)

    def set_age(self, age):
        self.age = age


cat1 = Cat('Squeaky', 3)
cat1.name
cat1.age
cat1.get_name()
cat1.meow()
cat1.get_age()
cat1.set_age(2)
cat1.get_age()


class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max):
        self.name = name
        self.max = max
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


stu1 = Student('Kyler', 19, 97)
stu2 = Student('Anya', 19, 89)
stu3 = Student('Kendra', 20, 76)

course = Course('Astronomy 101', 5)

course.add_students(stu1)
course.add_students(stu2)
course.add_students(stu3)

print(course.get_average_grade())

# inheritance - say we have two classes that are similar
# the two below have the same attributes but different speech methods


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self)
    print('meow')


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self)
    print('woof')


# inheritance allows us to make a single class with the common attributes

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.age} and my name is {self.name}.')


# by putting the Pet class name in parentheses, the new specific pets
# inherit the attributes and show method of the parent class Pet

class Kawawat(Pet):
    def speak(self):
        print('meew meew')


class Dowawat(Pet):
    def speak(self):
        print('wowoowoof')


p = Pet('Squawky', 19)
p.show()

# the two specific pets send their arguments to become attributes of the
# parent Pet class. when using the SHOW method, their specific arguments
# are fed in as attributes. the SHOW method is inherited as well.
# Inheritance reduces repitition in object / class definitions
k = Kawawat('Spooky', 2)
k.show()
k.speak()

d = Dowawat('Sparky', 1)
d.show()
d.speak()
