import random
from card import Card
# DECK CLASS OUTLINE

# Instantiate a new deck
#   Create all 52 cards of a deck
#   Hold a list of card objects

# Shuffle the deck through a method call
#   Random library, shuffle function

# Deal cards from the deck
#   Use the pop method from the deck list, pop pulls out a certain item from a list

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# list of ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# dictionary that maps values to card names
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Deck:

    # suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

    # # list of ranks
    # ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    #          'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    # # dictionary that maps values to card names
    # values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    #           'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self):
        # deck starts as an empty list
        self.all_cards = []
        #
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # method to shuffle the cards randomly
    def shuffle(self):
        random.shuffle(self.all_cards)

    # method to pull out one card
    def deal_one(self):
        return self.all_cards.pop()
