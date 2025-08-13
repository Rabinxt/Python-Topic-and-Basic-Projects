# json import
import json

# json example
json_data = {
    "name": "Rabin",
    "age": 22,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "is_student": True
}
python_obj = {"city": "Kathmandu", "country": "Nepal"} 

# Convert JSON → Python
# 1. Why convert JSON → Python?
# JSON is the format used for storing or sending data (files, APIs, etc.).
# When we read JSON, it’s just a string in Python.
# To work with it (loop, index, update values), we need to turn it into Python data types like dict or list.
python_data = json.loads(json_data)

# Convert Python → JSON
# 2. Why convert Python → JSON?
# When saving or sending data to another program, database, or API, they don’t understand Python’s objects — they expect a standard format like JSON.

# JSON is language-independent — JavaScript, Python, Java, etc., all understand it.
json_str = json.dumps(python_obj, indent=4)
print(json_str)

# Write to JSON file
with open("students.json", "w") as file:
    json.dump(json_data, file, indent=4)

# Read from JSON file
with open("students.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)