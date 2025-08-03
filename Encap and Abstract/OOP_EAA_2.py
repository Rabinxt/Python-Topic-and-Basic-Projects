# Project: Secure Employee Payroll System
# What you will build:
# An abstract base class Employee that defines:
# Abstract methods for calculate_pay() and display_info()
# Encapsulated private salary attribute (__salary) with getter and setter that 
# validate salary (e.g., salary can't be negative)
# Concrete subclasses that implement Employee:
# FullTimeEmployee (fixed salary + bonus)
# PartTimeEmployee (hourly rate × hours worked)
# Use encapsulation to protect sensitive data (salary), provide validation via getters/setters,
# and use abstraction to enforce implementation of payroll-related methods.
# Project requirements
# Abstract class Employee:
# Private attribute: __salary
# Property getter and setter for salary (salary ≥ 0)
# Abstract methods:
# calculate_pay() — calculate total pay
# display_info() — print employee details
# Subclass FullTimeEmployee:
# Additional attribute: bonus
# calculate_pay() returns salary + bonus
# Implements display_info()
# Subclass PartTimeEmployee:
# Additional attributes: hourly_rate, hours_worked
# calculate_pay() returns hourly_rate × hours_worked
# Implements display_info()

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            print("Invalid salary!")
        else:
            self.__salary = amount

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus

    def display_info(self):
        return f"FullTimeEmployee {self.name}: Total pay is {self.calculate_pay()}"

class PartTimeEmployee(Employee):
    def __init__(self, name, salary, hours_worked, hourly_rate=50):
        super().__init__(name, salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

    def display_info(self):
        return f"PartTimeEmployee {self.name}: Total pay is {self.calculate_pay()}"


FullWorker1 = FullTimeEmployee("Rabin", 5000, 1000)
print(FullWorker1.calculate_pay())
print(FullWorker1.display_info())

PartWorker1 = PartTimeEmployee("Sita", 0, 120, 40)
print(PartWorker1.calculate_pay())
print(PartWorker1.display_info())



