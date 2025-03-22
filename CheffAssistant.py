import json
import os

class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename

        # Shared ingredient stock
        self.ingredients = {
            "Steak": 10,
            "Potatoes": 20,
            "Garlic Butter": 5,
            "Asparagus": 15,
            "Salmon": 8,
            "Lemon": 10,
            "Chicken Breast": 10,
            "Pasta": 15,
            "Alfredo Sauce": 8,
            "Buns": 12,
            "Beef Patty": 10,
            "Tomato": 8,
            "Cheese": 10,
            "Carrots": 12,
            "Celery": 10,
            "Noodles": 15,
            "Broth": 8
        }

        # Meal recipes (how much of each ingredient a dish uses)
        self.meal_recipes = {
            "Steak Dinner": {"Steak": 1, "Potatoes": 2, "Garlic Butter": 1, "Asparagus": 3},
            "Salmon Dinner": {"Salmon": 1, "Lemon": 1, "Asparagus": 3},
            "Chicken Alfredo": {"Chicken Breast": 1, "Pasta": 2, "Alfredo Sauce": 1},
            "Burger": {"Buns": 2, "Beef Patty": 1, "Tomato": 1, "Cheese": 1, "Potatoes": 3},
            "Chicken Soup": {"Chicken Breast": 1, "Carrots": 2, "Celery": 2, "Noodles": 1, "Broth": 1}
        }

        self.usage_history = {ingredient: [] for ingredient in self.ingredients}

        self.load_inventory()

    def save_inventory(self):
        with open(self.filename, "w") as file:
            json.dump(self.ingredients, file, indent=4)
        print(f"Inventory saved successfully at: {os.path.abspath(self.filename)}")

    def load_inventory(self):
        try:
            with open(self.filename, "r") as file:
                self.ingredients = json.load(file)
            print("Inventory loaded successfully.")
        except FileNotFoundError:
            print("No saved inventory found. Using default values.")

    def place_order(self, meal):
        if meal not in self.meal_recipes:
            print("Meal not found!")
            return False

        recipe = self.meal_recipes[meal]

        # Check if all ingredients are available
        for ingredient, amount_needed in recipe.items():
            if self.ingredients.get(ingredient, 0) < amount_needed:
                print(f"Not enough {ingredient} to make {meal}. Restock needed.")
                return False

        # Deduct ingredients
        for ingredient, amount_needed in recipe.items():
            self.ingredients[ingredient] -= amount_needed
            self.usage_history[ingredient].append(-amount_needed)

        self.save_inventory()
        print(f"{meal} ordered successfully.")
        return True

    def restock_ingredient(self, ingredient, amount):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += amount
            self.usage_history[ingredient].append(amount)
            self.save_inventory()
            print(f"Restocked {ingredient} by {amount} units.")
        else:
            print(f"Ingredient '{ingredient}' not found in inventory.")
