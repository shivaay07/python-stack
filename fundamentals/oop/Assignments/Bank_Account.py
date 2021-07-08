class BankAccount:
    def __init__(self, int_rate = 1, balance = 0):
        int_rate = int_rate/100
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    # def withdraw(self,amount):
    #     self.balance -= amount
    #     print(self.balance)
    #     return self
    
    def withdraw(self,amount):
        if self.balance <= 0:
            print("Insufficient funds: Charginga $5 fee and deduct $5")
            self.balance = self.balance - 5
        else:
            self.balance -= amount
        print(self.balance)
        return self

    def display_account_info(self):
        print (f"Balance {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance * self.int_rate
            print (self.balance)
        return self


PNB = BankAccount(int_rate=2)
SBI = BankAccount()

PNB.deposit(420)
PNB.withdraw(200)
PNB.yield_interest()


