import json

# Sample data (list of dictionaries)
data = [
    {"name": "Shreya", "age": 18, "city": "Pune"},
    {"name": "Amit", "age": 20, "city": "Mumbai"},
    {"name": "Riya", "age": 19, "city": "Delhi"}
]

# Create JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully !")