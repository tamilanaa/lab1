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

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

class List():
    def __init__(self, a):
        self.a = a
    def filtering(self):
        return list(filter(lambda num : isPrime(num), self.a))

myList = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(myList.filtering())