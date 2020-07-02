
# CARD CLASS OUTLINE
# Each suit should have:14 cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# list of ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# dictionary that maps values to card names
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():

    # class wide attributes here:

    # # list of card suits
    # suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

    # # list of ranks
    # ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    #          'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    # # dictionary that maps values to card names
    # values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    #           'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # this maps the integer value from the class available dictionary
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# a_card = Card("Hearts", "Three")
# print(a_card)
