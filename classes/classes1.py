
# basic class setup:


class Cat:

    # class object attributes - these can be thought of as "constant" attributes
    # all members of the class would share these attributes
    # "self" is not needed because it is constant and does not change!
    # these go above the class constructor
    regnum = 'Animalia'
    phylum = 'Chordata'
    classis = 'Mammalia'
    classificationId = 89

    # constructor for the class
    # the constructor assigns attributes to each object/instance of the class
    # these attributes can change per instance, each cat below has different attributes
    def __init__(self, breed, fur, adult):
        self.breed = breed  # this takes the argument and assigns it to the attributes name
        self.fur = fur
        self.adult = adult


# creating a new instance of Cat and assigning attributes
twinky = Cat('Siamese', 'White-pointe', True)
twinky.breed    # an instance attribute
twinky.adult    # an instance attribute
twinky.fur      # an instance attribute
twinky.classificationId     # a class attribute (shared by all cats)
twinky.regnum               # a class attribute

# creating a new instance of Cat and assigning attributes
# using verbose arguments
gatto = Cat(breed='Tabby', fur='Tuxedo', adult=False)
gatto.breed     # an instance attribute
gatto.adult     # an instance attribute
gatto.fur       # an instance attribute
gatto.classificationId      # a class attribute
gatto.regnum                # a class attribute
