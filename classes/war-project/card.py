import random

# list of card suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# dictionary that maps values to card names
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# list of ranks


# CARD CLASS OUTLINE
# Each card should have:14*4

#   Suit
#   Rank
#   Value (as int)
class Card():

    # class wide attributes here:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        # this maps the integer value from the class available dictionary
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


three_of_clubs = Card('Clubs', 'Three')
three_of_clubs.rank
three_of_clubs.suit
three_of_clubs.value


# DECK CLASS OUTLINE

# Instantiate a new deck
#   Create all 52 cards of a deck
#   Hold a list of card objects

# Shuffle the deck through a method call
#   Random library, shuffle function

# Deal cards from the deck
#   Use the pop method from the deck list, pop pulls out a certain item from a list

class Deck:

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


new_deck = Deck()
print('the new deck has: ' + str(len(new_deck.all_cards)) + ' cards')

# view individual cards
top_card = new_deck.all_cards[0]
bottom_card = new_deck.all_cards[-1]
print(top_card)
print(bottom_card)
new_deck

# view the entire deck
for card in new_deck.all_cards:
    print(card)

# shuffle the cards
new_deck.shuffle()
bottom_card = new_deck.all_cards[-1]
print(bottom_card)

# view the shuffled deck
for card in new_deck.all_cards:
    print(card)

# deal a card, pop takes the last item in the list
# we use POP because a deck will be face down, so the bottom card.. the last item in the list,
# will actually be the top physical, and dealt card!
bottom_card = new_deck.all_cards[-1]
print(bottom_card)
a_card = new_deck.deal_one()
print(a_card)

# after the deal, check the number of cards in the list:
len(new_deck.all_cards)
print('the deck now has: ' + str(len(new_deck.all_cards)) + ' cards')


# PLAYER CLASS OUTLINE
# This class holds a players current LIST of cards
#   Players should be able to add or remove cards from their hand (list of cards)
#   Players should be able to add single or multiple cards from their hand
#   Need to visualize the placement of the cards from a physical hand


# Card deck model in python
# Cards     A   B   C    D
# Position  0   1   2   -1
# List = [A,B,C,D]
# The "top" is at position 0
# The "bottom" is at position -1

# SINGLE CARD ACTIONS
# Top of Hand... will be LIST.pop(0)
# Add a card... will be LIST.append(card)

# MULTI CARD ACTIONS
# New cards  = [E, F]
# Add to the list by using the extend list method ... LIST.extend([E,F])
# The cards will be added to the end of the list.
# Do not use append, it will only append a nested list!

class Player:

    def __init__(self, name):
        self.name = name
        # an empty hand of cards
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):  # check if new cards are in a list (multi)
            self.all_cards.extend(new_cards)
        else:  # else if a single card
            self.all_cards.append(new_cards)

    def __str__(self):
        # print('Player ' + self.name + ' has ' + len(self.all_cards) + ' cards.')
        return f'Player {self.name} has {len(self.all_cards)} cards'


Lola = Player("Lola")
print(Lola)

# look at the last pulled card
print(a_card)

# add it to the players hand
Lola.add_cards(a_card)
print(Lola)

# view all the players cards
for card in Lola.all_cards:
    print(card)

# see the card at index 0 - just this first one for now...
print(Lola.all_cards[0])

# test that we can add multiple cards as a list:
Lola.add_cards([a_card, a_card, a_card])

for card in Lola.all_cards:
    print(card)

print(Lola)

# test that we can remove a card (it will be the top card at position 0)
Lola.all_cards.pop(0)
print(Lola)
for card in Lola.all_cards:
    print(card)
