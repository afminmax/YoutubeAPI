from deck import Deck
from player import Player


# deck = Deck()

# for card in deck.all_cards:
#     print(card)

# print('the new deck has: ' + str(len(deck.all_cards)) + ' cards')

# deck.shuffle()


# 1. Create the Players
player1 = Player('P1')
player2 = Player('P2')

# 2. Create the Deck
deck = Deck()
deck.shuffle()

# 3. Deal the cards
# There are 52 cards. 26 cards for each player.
# We deal the cards two at a time.
for x in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())

# for card in player1.all_cards:
#     print(card)

# print(len(player1.all_cards))

# 4. Turn on the game
game_on = True

# 5.
round_num = 0

while game_on:

    # count the round
    round_num += 1
    print(f'Round {round_num}!')
