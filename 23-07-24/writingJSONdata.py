import json

def write_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


data = {"name": "John", "age": 30, "city": "New York"}
write_json(data, "output.json")
