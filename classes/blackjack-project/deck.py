import random
from card import Card


class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

    # list of ranks
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    # dictionary that maps values to card names
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
              'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        # deck starts as an empty list
        self.deck = []

        # deck building loop
        for suit in self.suits:
            for rank in self.ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    # print function to see deck contents
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp + '\n... Num of Cards: ' + str(len(self.deck))

    # method to shuffle the cards randomly
    def shuffle(self):
        random.shuffle(self.deck)

    # method to pull out one card
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# inplay_deck = Deck()
# print(inplay_deck)
# inplay_deck.shuffle()
# print(inplay_deck)
