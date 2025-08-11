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
python_data = json.loads(json_data)

# Convert Python → JSON
json_str = json.dumps(python_obj, indent=4)
print(json_str)

# Write to JSON file
with open("students.json", "w") as file:
    json.dump(json_data, file, indent=4)

# Read from JSON file
with open("students.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)