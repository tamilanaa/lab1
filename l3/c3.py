#5 Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
#  Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals,
#  and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money
        if(self.balance < 0):
            print("You have not enough money")
        else:
            print(self.balance)

wallet = Account("Sabina", 50000)
wallet.deposit(5000)
wallet.withdraw(100000)