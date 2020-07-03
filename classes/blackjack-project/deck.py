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
        self.all_cards = []

        for suit in self.suits:
            for rank in self.ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # method to shuffle the cards randomly
    def shuffle(self):
        random.shuffle(self.all_cards)

    # method to pull out one card
    def deal_one(self):
        return self.all_cards.pop()


deck = Deck()
print(deck)

for card in deck.all_cards:
    print(card)

print('the new deck has: ' + str(len(deck.all_cards)) + ' cards')

deck.shuffle()
for card in deck.all_cards:
    print(card)
print('the shuffled deck has: ' + str(len(deck.all_cards)) + ' cards')
