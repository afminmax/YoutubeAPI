from deck import Deck
from chips import Chips
from hand import Hand

# helper functions to facilitate the game

# function to take a bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips to bet?'))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed your current amount' + chips.total)


# a function for taking hits
def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# a function prompting the player to hit or stand
def hit_or_stand():
    global playing  # variable to control the on/off state for game play loop

    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':  # normalize first hit character
            hit(deck, hand)

        elif x[0].lower() == 's'
        print('Player stands, dealers turn')
        playing = False


# functions for end of game scenarios
def player_busts(player, dealer, chips):
    print('Bust player')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Bust dealer')
    chips.lose_bet()


def dealer_winds(player, dealer, chips):
    print('Dealer wins!')
    chips.win_bet()


def push(player, dealer, chips):
    print('Dealer and player tie! Push!')
