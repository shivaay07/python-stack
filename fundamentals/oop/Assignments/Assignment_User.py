
class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount



Shivam = User("Shivam Dutta", "d07@gmail.com")
Vishal = User("Vishal Duggal", "d28@gmail.com")
Munish = User("Munish Arora", "d04@gmail.com")


Shivam.make_deposit(100)
Shivam.make_deposit(400)
Shivam.make_deposit(900)

Shivam.make_withdrawl(200)

Shivam.display_user_balance()

Vishal.make_deposit(1100)
Vishal.make_deposit(100)

Vishal.make_withdrawl(200)
Vishal.make_withdrawl(200)

Vishal.display_user_balance()

Munish.make_deposit(1400)

Munish.make_withdrawl(200)
Munish.make_withdrawl(200)
Munish.make_withdrawl(100)

Munish.display_user_balance()

Shivam.transfer_money(Munish, 300)

Shivam.display_user_balance()
Munish.display_user_balance()