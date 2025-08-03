# Project 1: Number Divider (Basic Exception Handling)
# Goal: Learn how try, except/catch, finally work.
# Requirements:
# Take two numbers as input (or hardcode for now).
# Try to divide them.
# If denominator is 0  show error message.
# Always print Operation Completed in finally.
# Hints:
# In Python: ZeroDivisionError
# In JS: throw new Error("...") and catch with catch(e).

class NumberDivider:
    def Divider(self, a, b):
        try:
            result = a / b
            return result
        except:
            return "Code error"
    def Completion_method(self):
        print("Code Finally Executed")

class_handler = NumberDivider()
Numbers = [
    class_handler.Divider(14,2),
    class_handler.Divider(14,0),
    class_handler.Divider(14,2)
]
for number in Numbers:
    print(number)
    class_handler.Completion_method()