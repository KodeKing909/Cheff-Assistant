import json
import os

filename = "inventory.json"

# Define the updated ingredient-based inventory structure
updated_inventory = {
    "Steak": 98,
    "Potatoes": 106,
    "Garlic Butter": 198,
    "Asparagus": 594,
    "Salmon": 800,
    "Lemon": 100,
    "Chicken Breast": 100,
    "Pasta": 150,
    "Alfredo Sauce": 80,
    "Buns": 100,
    "Beef Patty": 99,
    "Tomato": 79,
    "Cheese": 99,
    "Carrots": 120,
    "Celery": 150,
    "Noodles": 150,
    "Broth": 99
}

# Remove the old file if it exists
if os.path.exists(filename):
    os.remove(filename)
    print(f"Deleted old inventory file: {filename}")

# Create a new file with the updated inventory
with open(filename, "w") as file:
    json.dump(updated_inventory, file, indent=4)

print(f"New ingredient-based inventory file '{filename}' created successfully.")