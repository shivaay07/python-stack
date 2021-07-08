class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount



Shivam = User("Shivam Dutta", "d07@gmail.com")
Vishal = User("Vishal Duggal", "d28@gmail.com")
Munish = User("Munish Arora", "d04@gmail.com")


Shivam.make_deposit(100).make_deposit(400).make_withdrawl(200).display_user_balance()