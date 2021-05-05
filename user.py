class User:    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: "+ self.name + ", Balance: " + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        print("After $ "+str(amount)+ " money transfer from "+self.name + " to "+other_user.name)
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
tom = User("Tom Heckman", "tom@gmail.com")

guido.make_deposit(50).make_deposit(100).make_deposit(20).make_withdrawal(30).display_user_balance()


monty.make_deposit(100).make_deposit(300).make_withdrawal(50).make_withdrawal(20).display_user_balance()

tom.make_deposit(400).make_withdrawal(50).make_withdrawal(100).make_withdrawal(20).display_user_balance()

tom.transfer_money(guido, 20)
