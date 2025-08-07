# Step 1: List of student records
students = [
    ("Rabin", 85),
    ("Sita", 35),
    ("Hari", 67),
    ("Gita", 22),
    ("Bikash", 91),
    ("Nita", 39)
]
result_dict = {name: "Pass" if marks >= 40 else "Fail" for name, marks in students}
print(result_dict)

