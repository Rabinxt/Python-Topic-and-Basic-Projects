# Encapsulation in Python - Detailed Notes

class Account:
    def __init__(self, balance):
        # Private variable using name mangling
        # We can also use _balance for private
        self.__balance = balance  
    
    @property
    def balance(self):
        """Getter method for balance.
        Allows access to the private variable __balance
        like a public attribute."""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Setter method for balance.
        Validates the input and updates __balance.
        This prevents invalid values like negative balance."""
        if amount < 0:
            print("Invalid balance! Cannot set negative value.")
        else:
            # Here we add amount to existing balance to simulate deposit
            self.__balance += amount

# -----------------------------------------
# Usage and important notes on property setter/getter behavior:

acc = Account(1000)

# Access balance via getter property
print(acc.balance)  # Output: 1000

# Update balance via setter property (adds 200 to balance)
acc.balance = 200

# Get updated balance via getter
print(acc.balance)  # Output: 1200

# Trying to set invalid negative balance
acc.balance = -500  # Output: Invalid balance! Cannot set negative value.

# Important:
# When doing 'acc.balance = 200', Python calls the setter.
# The setter does NOT return a value; it only updates internal state.
# Therefore, you cannot do 'store = acc.balance = 200' to get updated balance in one line,
# because 'store' will be assigned the value 200, not the updated balance.
# To get the updated balance, you must call the getter separately:
store = acc.balance
print(store)  # Output: 1200

# -----------------------------------------
# Summary:
# - Use private variables (prefix with __) to hide data.
# - Use @property decorator to create a getter.
# - Use @propertyname.setter decorator to create a setter with validation.
# - This encapsulation protects internal state and enforces rules.
# - Setter is for assignment only; it does not return values.
