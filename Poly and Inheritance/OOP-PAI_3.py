# Project 3: Game Characters with Multilevel + Hybrid Inheritance
# Concepts Covered:
# Multilevel inheritance
# Hybrid inheritance (multiple + multilevel combined)
# Use of super() and method overriding
# MRO in a complex hierarchy
# Polymorphism with characters’ attack() method
# Project Requirements:
# Base class: Character
# Attributes: name, level
# Method: attack() returns generic attack message
# Subclasses:
# Warrior(Character)
# Overrides attack() to do a strong melee attack
# Mage(Character)
# Overrides attack() to do a magical attack
# Hybrid subclass:
# HybridCharacter(Warrior, Mage)
# Combines melee and magic
# Overrides attack() and uses super() to combine attacks
# Demonstrate:
# Create instances of Warrior, Mage, and HybridCharacter
# Call attack() on each and show polymorphic behavior
# Print HybridCharacter.__mro__ to see method resolution order

class Character:
    def __init__(self,name, level):
        self.name = name
        self.level = level
     
    def attack(self):
        return f"{self.name} performs a generic attack at level {self.level}"
        
class Warrior(Character):
    def attack(self):
        base = super().attack()
        return f"{base} → {self.name} strikes with a mighty sword"
        
class Mage(Character):
    def attack(self):
        base = super().attack()
        return f"{base} → {self.name} casts a powerful spell"

class HybridCharacter(Warrior, Mage):
    def attack(self):
        base = super().attack()
        return f"{base} → {self.name} unleashes hybrid fury"

w = Warrior("Thor", 5)
m = Mage("Merlin", 7)
h = HybridCharacter("Gandalf", 10)

print(h.attack())

print(HybridCharacter.__mro__)





