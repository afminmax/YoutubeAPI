class Account:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def accountInfo(self):
        print('Account owner: ' + self.name)
        print('Account balance: ' + str(self.amount))

    def deposit(self, credit):
        pass

    def withdraw(self, debit):
        pass


account1 = Account('alyna', 100)
account1.name
account1.amount


account1.accountInfo()
