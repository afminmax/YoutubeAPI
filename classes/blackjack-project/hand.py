from deck import Deck

# Hand class will represent which cards are in someones hands.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# list of ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# dictionary that maps values to card names
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Hand:
    def __init__(self):
        self.cards = []  # start with empty list.
        self.value = 0  # start with zero value for the hand.
        self.aces = 0   # add an attribute to keep track of aces.

    def add_card(self, card):
        # card passed in from Deck class via deal method.
        # from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)

        # calculate the value of the card by using the dictionary value
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # if total value > 21, and an ace still in the hand, then
        # change the ace to equal 1 instead of 11
        #
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1  # remove 1 from the count of aces


# checks....

# build a deck
test_deck = Deck()
test_deck.shuffle()
print(test_deck)

# build a player
test_player = Hand()
# get a card from the deck
pulled_card = test_deck.deal()
print(pulled_card)
# add the card to the players hand
test_player.add_card(pulled_card)
print(test_player.value)

# add another card
test_player.add_card(test_deck.deal())
print(test_player.value)


# truthiness....
# num = 0
# one = 1
# two = 2

# if 1:
#     print('True')
