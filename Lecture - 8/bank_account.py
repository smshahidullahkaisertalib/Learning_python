class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("BDT", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance -= amount
        print("BDT", amount, "was credited")
        print("Total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(101, 10000)
acc1.debit(1000)
acc1.credit(100)