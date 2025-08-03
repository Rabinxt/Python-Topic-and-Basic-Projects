# Project 3 – Student Grade Manager
# 🎯 Concepts
# Custom exceptions
# Try–except–finally
# Validation of input
# What to Do
# Custom Exceptions
# InvalidGradeError → grade not between 0–100
# NoStudentsError → no students when calculating average
# Student Class
# Has: name, grade
# Check grade in constructor (raise InvalidGradeError if wrong)
# GradeManager Class
# Keeps list of students
# add_student(name, grade) → adds after validation
# calculate_average() → average of grades (raise NoStudentsError if list empty)
# display_students() → show all
# Testing
# Add valid and invalid students
# Try average when list empty and when filled
# # Use finally to print "Operation Completed"
# -------------------------------
# Custom Exceptions
# -------------------------------
class InvalidGradeError(Exception):
    """Raised when grade is not between 0-100."""
    pass

class NoStudentsError(Exception):
    """Raised when there are no students in the list."""
    pass

class Student:
    def __init__(self,name,grade):
        if not (0 <= grade <= 100):
            raise InvalidGradeError(f"Invalid grade {grade}. Must be between 0 and 100.")
        self.name = name
        self.grade = grade

class GradeManager:
    def __init__(self):
        self.Students = []


    def add_student(self, name, grade):
        try:
            self.Students.append(Student(name, grade))
            print(f"Student {name} added sucessfully")
        except InvalidGradeError as IGE:
            print(f"Error: {IGE}")


    def calculate_average(self):
        try:
            if len(self.Students) == 0:
                raise NoStudentsError("No Students in List")
            total = sum(students.grade for students in self.Students)
            average = total / len(self.Students)
            return average
        except NoStudentsError as NSE:
            return f"Error: {NSE}"


    def display_students(self):
        try:
            for student in self.Students:
                print(student.name)

        except NoStudentsError as NSE:
            return f"Error: {NSE}"

# -------------------------------
# Testing
# -------------------------------
manager = GradeManager()
manager.add_student("Rabin", 95)
manager.add_student("Sita", 105)     
manager.add_student("Gita", 85)      

print("\nStudents List:")
manager.display_students()

print("\nAverage Grade:")
print(manager.calculate_average())