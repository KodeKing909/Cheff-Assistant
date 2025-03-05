import json

filename = "inventory.json"

try:
    with open(filename, "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("No saved inventory file found.")
