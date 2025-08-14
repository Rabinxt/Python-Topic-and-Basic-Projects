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

# -----------------------------
# 3. READING CSV (normal way)
# -----------------------------
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    
    print("\n📄 Reading CSV (list format):")
    for row in reader:
        print(row)  # Each row is a list of values (strings)

# -----------------------------
# 4. READING CSV AS DICTIONARY (DictReader)
# -----------------------------
with open("students.csv", mode="r") as file:
    dict_reader = csv.DictReader(file)  # Uses first row as keys
    
    print("\n📄 Reading CSV (dictionary format):")
    for row in dict_reader:
        print(row)  # Each row is a dictionary {column_name: value}

# -----------------------------
# 5. WRITING CSV AS DICTIONARY (DictWriter)
# -----------------------------
# Overwrite with new data
with open("students_dict.csv", mode="w", newline="") as file:
    fieldnames = ["Name", "Age", "Grade"]  # Keys for dictionary
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    dict_writer.writeheader()  # Write the header row
    
    dict_writer.writerow({"Name": "Hari", "Age": 20, "Grade": "A"})
    dict_writer.writerow({"Name": "Anita", "Age": 21, "Grade": "B+"})
print("✅ DictWriter writing completed.")
