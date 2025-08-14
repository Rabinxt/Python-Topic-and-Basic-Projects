import csv  # Built-in module for handling CSV files

# -----------------------------
# 1. WRITING CSV (overwrite old data)
# -----------------------------
# Open the file in 'w' mode (write mode) — this erases old content if file exists
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)  # Create a writer object
    
    # Writing the header row
    writer.writerow(["Name", "Age", "Grade"])
    
    # Writing multiple rows of student data
    writer.writerow(["Rabin", 20, "A"])
    writer.writerow(["Sita", 19, "B"])
    writer.writerow(["Gopal", 21, "A+"])
print("✅ Writing completed.")

# -----------------------------
# 2. APPENDING TO CSV (adding new data without removing old data)
# -----------------------------
# 'a' mode = append mode
with open("students.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Mina", 22, "B+"])
print("✅ Appending completed.")
