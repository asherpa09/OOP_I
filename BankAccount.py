class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance-= amount
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print("Current Balance is: $" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance = self.balance * 0.01
        return self
checkingAccount = BankAccount(0.01, 0)
savingAccount = BankAccount(0.01, 0)

checkingAccount.deposit(100).deposit(200).deposit(200).withdraw(600).yield_interest().display_account_info()
savingAccount.deposit(500).deposit(300).withdraw(5).withdraw(10).withdraw(800).withdraw(200).display_account_info()

