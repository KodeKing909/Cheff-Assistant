import json
import os

class Inventory:
    """
    The Inventory class manages restaurant ingredients, meal recipes,
    placing orders, restocking, and tracking ingredient usage history
    for analytics purposes.
    """
    def __init__(self, filename="inventory.json"):
        # Filename to save the inventory to
        self.filename = filename

        # File to persist usage history (so it's not lost between runs)
        self.history_file = "usage_history.json"

        # Dictionary holding current stock for each ingredient
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

        # Dictionary defining how many units of each ingredient are needed for each meal
        self.meal_recipes = {
            "Steak Dinner": {"Steak": 1, "Potatoes": 2, "Garlic Butter": 1, "Asparagus": 3},
            "Salmon Dinner": {"Salmon": 1, "Lemon": 1, "Asparagus": 3},
            "Chicken Alfredo": {"Chicken Breast": 1, "Pasta": 2, "Alfredo Sauce": 1},
            "Burger": {"Buns": 2, "Beef Patty": 1, "Tomato": 1, "Cheese": 1, "Potatoes": 3},
            "Chicken Soup": {"Chicken Breast": 1, "Carrots": 2, "Celery": 2, "Noodles": 1, "Broth": 1}
        }

        # Dictionary tracking usage (consumption or restocking) of each ingredient
        # Example: { "Steak": [-1, -1, +10] }
        self.usage_history = {ingredient: [] for ingredient in self.ingredients}

        # Load inventory and usage history from disk (if available)
        self.load_inventory()

    def save_inventory(self):
        """
        Saves both the ingredient inventory and usage history to disk as JSON files.
        """
        with open(self.filename, "w") as file:
            json.dump(self.ingredients, file, indent=4)

        with open(self.history_file, "w") as file:
            json.dump(self.usage_history, file, indent=4)

        print(f"Inventory saved successfully at: {os.path.abspath(self.filename)}")

    def load_inventory(self):
        """
        Loads ingredient inventory and usage history from disk, if files exist.
        If not, default values are used.
        """
        try:
            with open(self.filename, "r") as file:
                self.ingredients = json.load(file)
            print("Inventory loaded successfully.")
        except FileNotFoundError:
            print("No saved inventory found. Using default values.")

        try:
            with open(self.history_file, "r") as file:
                self.usage_history = json.load(file)
        except FileNotFoundError:
            print("No usage history found. Starting fresh.")

    def place_order(self, meal):
        """
        Deducts the required ingredients for a given meal.
        Logs usage in `usage_history` and saves changes to disk.

        Args:
            meal (str): The name of the meal to order.

        Returns:
            bool: True if order successful, False if not enough ingredients.
        """
        if meal not in self.meal_recipes:
            print("Meal not found!")
            return False

        recipe = self.meal_recipes[meal]

        # Check if all ingredients are available in sufficient quantities
        for ingredient, amount_needed in recipe.items():
            if self.ingredients.get(ingredient, 0) < amount_needed:
                print(f"Not enough {ingredient} to make {meal}. Restock needed.")
                return False

        # Deduct ingredients and log consumption
        for ingredient, amount_needed in recipe.items():
            self.ingredients[ingredient] -= amount_needed
            self.usage_history[ingredient].append(-amount_needed)

        self.save_inventory()
        print(f"{meal} ordered successfully.")
        return True

    def restock_ingredient(self, ingredient, amount):
        """
        Increases the inventory of a specific ingredient and logs the restock.

        Args:
            ingredient (str): The name of the ingredient to restock.
            amount (int): The number of units to add to stock.
        """
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += amount
            self.usage_history[ingredient].append(amount)
            self.save_inventory()
            print (f"Restocked {ingredient} by {amount} units. ")
        else:
            print(f"Ingredient '{ingredient}' not found in inventory.")
