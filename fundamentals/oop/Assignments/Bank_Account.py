class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 1, balance = 0):
        int_rate = int_rate/100
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
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
    @classmethod
    def all_balances(cls):
        sum = 0
        for accounts in cls.all_accounts:
            sum += account.balance
        return sum

PNB = BankAccount(int_rate=2)
SBI = BankAccount(int_rate=1)

PNB.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
SBI.deposit(200).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
