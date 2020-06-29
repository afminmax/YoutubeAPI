class Account:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def accountInfo(self):
        print('Account owner: ' + self.name)
        print('Account balance: ' + str(self.amount))

    def deposit(self, credit):
        self.amount = self.amount + credit
        print('deposit accepted, new balance: ' + str(self.amount))
        # return self.amount

    def withdraw(self, debit):
        if debit <= self.amount:
            self.amount = self.amount - debit
            print('withdrawal accepted, new balance: ' + str(self.amount))
        else:
            print('insufficient funds, debit not allowed.')

        # return self.amount


account1 = Account('alyna', 100)

account1.accountInfo()
account1.name
account1.amount


account1.deposit(500)

account1.withdraw(200)

account1.withdraw(450)

account1.amount
