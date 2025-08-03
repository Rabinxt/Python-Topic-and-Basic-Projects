# Project 2 (Medium) Payment System
# Concepts covered:
# Multiple inheritance (CombinedPayment inherits from two payment classes)
# super() in multiple inheritance
# MRO check (__mro__)
# Polymorphism in process_payment()
# Requirements:
# Base class: Payment
# Method: process_payment() (generic message)
# Subclasses:
# CreditCardPayment (inherits from Payment, overrides process_payment())
# PayPalPayment (inherits from Payment, overrides process_payment())
# Class: CombinedPayment
# Inherits from both CreditCardPayment and PayPalPayment
# Uses super() in process_payment()
# Prints MRO to show method resolution order
# Create a list of payment objects (CreditCardPayment, PayPalPayment, CombinedPayment) 
# and call process_payment() polymorphically.

class Payment:
    def __init__(self, details, amount):
        self.details = details
        self.amount = amount
    
    def process_payment(self):
        return f"Processing generic payment of {self.amount}"


class CreditCardPayment(Payment):
    def __init__(self, details, amount):
        super().__init__(details, amount)
    
    def process_payment(self):
        return f"Processing Credit Card payment of {self.amount}"


class PayPalPayment(Payment):
    def __init__(self, details, amount):
        super().__init__(details, amount)
    
    def process_payment(self):
        return f"Processing PayPal payment of {self.amount}"


class CombinedPayment(CreditCardPayment, PayPalPayment):
    def process_payment(self):
        result = super().process_payment()   # Calls CreditCardPayment first
        return f"{result} + PayPal split payment"


# Test
payments = [
    CreditCardPayment("Card: 1234", 100),
    PayPalPayment("PayPal: rabin@example.com", 50),
    CombinedPayment("Combo", 150)
]

for p in payments:
    print(p.process_payment())

# Check MRO
print(CombinedPayment.__mro__)

# key point to remember:
#   Mro goes like:
#     CombinedPayment → CreditCardPayment → PayPalPayment → Payment → object