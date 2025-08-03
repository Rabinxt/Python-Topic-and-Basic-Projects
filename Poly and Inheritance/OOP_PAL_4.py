# Project 4: Bank Transactions System (Hybrid + Multilevel Inheritance)
# Concepts Covered
# Hybrid inheritance: Multiple transaction types
# Multilevel inheritance: Special types of accounts
# super() chaining to process different steps
# MRO in a hybrid structure
# Polymorphism: Different transactions executed in one loop
# Project Requirements
# Base class: Account
# Attributes: owner, balance
# Method: process_transaction(amount) → basic debit/credit update
# Transaction types:
# Deposit(Account) → adds funds
# Withdraw(Account) → subtracts funds (if balance allows)
# Special Hybrid Transaction:
# Transfer(Withdraw, Deposit) → withdraw from one account, deposit into another
# Uses super() to call both Withdraw and Deposit processing
# Demonstrate:
# Create accounts
# Do a deposit, withdrawal, and transfer using polymorphism
# Show MRO of Transfer

class Account:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
        
    def process_transaction(self,amount):
        self.balance += amount
        return f"[{self.owner}] New balance: {self.balance}"
        
class Deposit(Account):
    pass

class Withdraw(Account):
    pass

class Transfer(Withdraw, Deposit):
    pass
