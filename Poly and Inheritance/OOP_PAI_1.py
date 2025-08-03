# 🔹 Level 1 (Easy) — Employee Management System (Single Inheritance + Polymorphism)
# Concepts:
# Single inheritance (Developer → Employee)
# super() to call parent constructor
# Method overriding
# Polymorphism (different bonus calculations)
# Requirements:
# Base class: Employee
# Attributes: name, salary
# Method: get_bonus() (default bonus: 5% of salary)
# Subclasses: Developer and Manager (inherit from Employee)
# Override get_bonus() (Developer: 10%, Manager: 15%)
# Create a list of employees (Developer and Manager) and call get_bonus() polymorphically.
# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_bonus(self):
        return self.salary *0.05
        
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language= programming_language
        
    def get_bonus(self):
        return self.salary * 0.10

class Manager(Developer):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size
        
    def get_bonus(self):
        return self.salary * 0.15
        
        
Rabin = Employee("rabin" , 20000)
print(Rabin.get_bonus())
Reejan = Developer("rabin" , 20000, "Python")
print(Reejan.get_bonus())
