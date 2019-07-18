class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return "Account owner:   {:10} \nAccount balance: ${}".format(self.owner, self.balance)
    def deposit(self, total):
        self.balance += total
        return 'Deposit accepted'
    def withdraw(self, total):
        if self.balance - total >= 0:
            self.balance -= total
            return "Withdraw accepted"
        else:
            return "Funds Unavaible!"
acct1 = Account('Jose',100)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))
print(acct1)
