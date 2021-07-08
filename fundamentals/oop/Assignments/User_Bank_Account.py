class BankAccount:
    # all_accounts = []
    def __init__(self, int_rate = 2, balance = 0):
        int_rate = int_rate/100
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_accounts.append(self)
    
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
    # @classmethod
    # def all_balances(cls):
    #     sum = 0
    #     for accounts in cls.all_accounts:
    #         sum += account.balance
    #     return sum

# PNB = BankAccount(int_rate=2)
# SBI = BankAccount(int_rate=1)

# PNB.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
# SBI.deposit(200).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount(int_rate = 2 , balance = 0)
        

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdraw(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    # def transfer_money(self, other_user, amount):
    #     other_user.account_balance += amount
    #     self.account_balance -= amount


Shivam = User("Shivam Dutta", "d07@gmail.com")
Vishal = User("Vishal Duggal", "d28@gmail.com")
Munish = User("Munish Arora", "d04@gmail.com")

Shivam.make_deposit(400).make_withdraw(200).display_user_balance()