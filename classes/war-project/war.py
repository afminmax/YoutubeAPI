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

    # count and print the round
    round_num += 1
    print('Round: ' + str(round_num))

    # check if a player is out of cards before the start of the round
    if len(player1.all_cards) == 0:
        print('Player 1, out of cards - Player 2 wins!')
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print('Player 2, out of cards - Player 1 wins!')
        game_on = False
        break

    # START A NEW ROUND - each player gets an empty list that holds their cards for the round
    # then, a card from their hand is added to their cards in play
    player1_cards = []
    player1_cards.append(player1.remove_one())

    player2_cards = []
    player2_cards.append(player2.remove_one())

    # compare the players hands (while at war)
    comparing = True

    while comparing:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            # print('P1: ' + str(player1_cards) + ' P2: ' + str(player2_cards)) <- need to figure out how to concatenate a list as string
            comparing = False

        elif player2_cards[-1].value > player1_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            # print('P1: ' + str(player1_cards) + ' P2: ' + str(player2_cards))
            comparing = False

        # war occurs when the players draw out the same card
        else:
            print('War')

            # check if the players have enough cards to conduct war:
            if len(player1.all_cards) < 3:
                print('Player 1 unable to declare war')
                print('Player 2 wins!')
                game_on = False
                break

            if len(player2.all_cards) < 3:
                print('Player 2 unable to declare war')
                print('Player 1 wins!')
                game_on = False
                break

            # if each player has enough cards for war, add the war cards:
            else:
                for num in range(3):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
