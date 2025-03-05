import json
import os

filename = "inventory.json"

# Define the updated inventory structure
updated_inventory = {
    "Steak Dinner": {"Steak": 10, "Potatoes": 20, "Garlic Butter": 5, "Asparagus": 5},
    "Salmon Dinner": {"Salmon": 8, "Lemon": 10, "Asparagus": 15},
    "Chicken Alfredo": {"Chicken Breast": 10, "Pasta": 15, "Alfredo Sauce": 8},
    "Burger": {"Buns": 12, "Beef Patty": 10, "Tomato": 8, "Cheese": 10, "Potatoes": 10},
    "Chicken Soup": {"Chicken Breast": 10, "Carrots": 12, "Celery": 10, "Noodles": 15, "Broth": 8}
}

# Remove the old file if it exists
if os.path.exists(filename):
    os.remove(filename)
    print(f"Deleted old inventory file: {filename}")

# Create a new file with the updated inventory
with open(filename, "w") as file:
    json.dump(updated_inventory, file, indent=4)

print(f"New inventory file '{filename}' created successfully.")

