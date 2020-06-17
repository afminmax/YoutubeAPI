
# basic class setup:


class Cat:

    # constructor for the class
    def __init__(self, breed, fur, adult):
        self.breed = breed  # this takes the argument and assigns it to the attributes name
        self.fur = fur
        self.adult = adult


# creating a new instance of Cat and assigning attributes
twinky = Cat('Siamese', 'White-pointe', True)
twinky.breed
twinky.adult
twinky.fur

# creating a new instance of Cat and assigning attributes
# using verbose arguments
gatto = Cat(breed='Tabby', fur='Tuxedo', adult=False)
gatto.breed
gatto.adult
gatto.fur
