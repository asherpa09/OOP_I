class User:    
    def __init__(self, name, email,int_rate=0.01):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=int_rate, balance=0)
    

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User: "+ self.name + ", Balance: " + str(self.account.balance))
        return self

    def transfer_money(self, other_user, amount):
        print("After $ "+str(amount)+ " money transfer from "+self.name + " to "+other_user.name)
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance-= amount
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance  - 5
        return self

    def display_account_info(self):
        print("Current Balance is: $" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

        
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
tom = User("Tom Heckman", "tom@gmail.com",0.05)
# checkingAccount = BankAccount(0.02, 0)
# savingAccount = BankAccount(0.02, 0)

guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(600).yield_interest().display_user_balance()
monty.make_deposit(500).make_deposit(300).make_withdrawal(5).make_withdrawal(10).make_withdrawal(800).make_withdrawal(200).display_user_balance()