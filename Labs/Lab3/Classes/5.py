class bank_account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Dear {self.owner}, not enough money on balance.")
            return 0
        self.balance -= amount

acc1 = bank_account("Peter", 1400)
acc1.deposit(800)
print(acc1.balance)
acc1.withdraw(3000)
print(acc1.balance)
acc1.withdraw(2000)
print(acc1.balance)