# The chips class tracks the state and value of the chips


class Chips:

    def __init__(self):
        self.total = 100  # this is just a default start
        self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet
