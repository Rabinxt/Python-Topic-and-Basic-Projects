# json import
import json

# json example
json_data = {
    "name": "Rabin",
    "age": 22,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "is_student": True
}

# Convert JSON → Python
python_data = json.loads(json_data)