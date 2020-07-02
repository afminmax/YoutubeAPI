import

# PLAYER CLASS OUTLINE
# This class holds a players current LIST of cards
#   Players should be able to add or remove cards from their hand (list of cards)
#   Players should be able to add single or multiple cards from their hand
#   Need to visualize the placement of the cards from a physical hand


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
