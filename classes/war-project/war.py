from deck import Deck
# from player import Player


deck = Deck()
print(deck)

for card in deck.all_cards:
    print(card)

print('the new deck has: ' + str(len(deck.all_cards)) + ' cards')
