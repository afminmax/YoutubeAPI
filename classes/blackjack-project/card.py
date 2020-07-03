# CARD CLASS

# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# # list of ranks
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
#          'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# # dictionary that maps values to card names
# values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
#           'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

    # list of ranks
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    # dictionary that maps values to card names
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
              'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # this maps the integer value from the class available dictionary
        self.value = self.values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# a_card = Card("Hearts", "Three")
# print(a_card)
# print(a_card.suit)
# print(a_card.value)
