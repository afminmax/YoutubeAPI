from deck import Deck
from chips import Chips
from hand import Hand


# declare a Boolean value to be used to control while loops.
# this is a common practice used to control the flow of the game.
playing = True


# helper functions to facilitate the game

# function to take a bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips to bet?  '))
        except ValueError:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total or chips.bet < 0:
                print(
                    'Sorry, your bet cannot exceed your current amount or be negative: ' + str(chips.total))
            else:
                break

# a function for taking hits


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


# a function prompting the player to hit or stand
def hit_or_stand(deck, hand):
    global playing  # variable to control the on/off state for game play loop

    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':  # normalize first hit character
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player stands, dealers turn')
            playing = False

        else:
            print('Sorry, please enter h or s keys only.')
            continue

        break

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


def dealer_wins(player, dealer, chips):
    print('Dealer wins!')
    chips.win_bet()


def push(player, dealer):
    print('Dealer and player tie! Push!')

# functions for showing hands


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# RUN THE GAME

while True:
    print('Welcome to Python Blackjack!')

    # 1. create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    # print(deck)

    # 2. setup the player and dealers initial hands
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())  # two cards!
    # print(player_hand)

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    # print(dealer_hand)

    # 3. setup the players chips
    player_chips = Chips()

    # 4. prompt player for their bet:
    take_bet(player_chips)

    # 5. show cards
    show_some(player_hand, dealer_hand)

    # 6. betting!
    while playing:  # this comes from the hit or stand function
        # prompt player to hit or stand
        hit_or_stand(deck, player_hand)

        # show cards (keep one from dealer hidden)
        show_some(player_hand, dealer_hand)

        # check if player busted and if so, break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # if player has not busted and is still in play
    # dealer plays until 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # show all dealer cards
        show_all(player_hand, dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # inform player of remaining chips
    print('\n Player total chips: ' + str(player_chips.total))

    # ask to play again
    new_game = input('Would you like to play again? y/n:  ')

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else:
        print('Thanks and play again')
