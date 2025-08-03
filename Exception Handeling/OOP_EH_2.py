# Project 2 – Custom Exception for Banking
# Concept: Creating your own exceptions
# Goal:
# Create a BankAccount class.
# Withdraw/Deposit money.
# Raise InsufficientFundsError if withdrawal is more than balance.
# Focus: Custom exception classes, raising exceptions manually.
class OutOfFund(Exception):
    pass
class BankAccount:
    def __init__(self, account, remainingBal):
        self.account = account
        self.remainingBal = remainingBal

    def Withdraw(self, withdrawAmt):
        try:
            if withdrawAmt > self.remainingBal :
                 raise OutOfFund("No Remaining Balance for withdrawal")
            else:
                self.remainingBal -= withdrawAmt
                return self.remainingBal
        except OutOfFund as of:
            return str(of)

    def Deposit(self, amount):
        self.remainingBal += amount
        return f"Account {self.account}: Deposit successful. New balance: {self.remainingBal}"

Accounts = [
     BankAccount(1000 , 30000),
     BankAccount(1001 , 40000),
     BankAccount(1002 , 1000)
]
for account in Accounts:
     print(account.Withdraw(10000))