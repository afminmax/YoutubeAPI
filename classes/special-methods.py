# SPECIAL METHODS (or DUNDER - double underscore) ALLOW YOU TO USE PYTHON NATIVE METHODS

mylist = ['venus', 'earth', 'mars']

# this system method provides the length of the list:
len(mylist)


# now, when we create a class and instantiate a new object, the system length method is not
# available for use:
class Moon():
    pass


mymoon = Moon()

# when trying to get a
len(mymoon)  # will generate an error: TypeError: object of type 'Moon' has no len()


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # the following special / dunder methods use the same name as the python system method
    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('the book object has been deleted')


mybook = Book('Python is cool', 'Je Suis', 60)

# note here that the print of the object 'mybook' normally just outputs the memory allocation of the book
# this output occurs if the special str method is NOT in the class definition
# # <__main__.Book object at 0x000002A1EDE6DEC8>
print(mybook)

# ...whereas a print of my list yields the actual list
print(mylist)

# to get a printout of what comprises the object, we can add a special method to, print out
# what data we want printed out from the class which is the __str__ method above.

# to get length, we use a 'len' special method

len(mybook)


# A side note; how to delete variables:::

del mybook
