import json
import os
          ## Dictionary to hold meals and their corresponging ingredients 
class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.ingredients = {
            "Steak Dinner": {"Steak": 10, "Potatoes": 20, "Garlic Butter": 5},
            "Salmon Dinner": {"Salmon": 8, "Lemon": 10, "Asparagus": 15},
            "Chicken Alfredo": {"Chicken Breast": 10, "Pasta": 15, "Alfredo Sauce": 8},
            "Burger": {"Buns": 12, "Beef Patty": 10, "Tomato": 8, "Cheese": 10},
            "Chicken Soup": {"Chicken": 10, "Carrots": 12, "Celery": 10, "Noodles": 15, "Broth": 8}
        }
        self.usage_history = {ingredient: [] for meal in self.ingredients for ingredient in self.ingredients[meal]}
        self.load_inventory()
    
    def save_inventory(self):
        with open(self.filename, "w") as file:
            json.dump(self.ingredients, file, indent=4)
        file_path = os.path.abspath(self.filename)
        print(f"Inventory saved successfully at: {file_path}")
    
    def load_inventory(self):
        try:
            with open(self.filename, "r") as file:
                self.ingredients = json.load(file)
            print("Inventory loaded successfully.")
        except FileNotFoundError:
            print("No saved inventory found. Using default values.")
    
    def place_order(self, meal):
        if meal in self.ingredients:
            required_ingredients = self.ingredients[meal]
            
            for ingredient in required_ingredients:
                if self.ingredients[meal][ingredient] < 1:
                    print(f"Not enough {ingredient} to make {meal}. Restock needed.")
                    return False
                                                ## Deducts the amount of ingredients used per meal every time order is placed. 
            if meal == "Steak Dinner":
                self.ingredients[meal]["Steak"] -= 1
                self.ingredients[meal]["Potatoes"] -= 2
                self.ingredients[meal]["Garlic Butter"] -= 1
            elif meal == "Salmon Dinner":
                self.ingredients[meal]["Salmon"] -= 1
                self.ingredients[meal]["Lemon"] -= 1
                self.ingredients[meal]["Asparagus"] -= 5
            elif meal == "Chicken Alfredo":
                self.ingredients[meal]["Chicken Breast"] -= 1
                self.ingredients[meal]["Pasta"] -= 1
                self.ingredients[meal]["Alfredo Sauce"] -= 1
            elif meal == "Burger":
                self.ingredients[meal]["Buns"] -= 2
                self.ingredients[meal]["Beef Patty"] -= 1
                self.ingredients[meal]["Tomato"] -= 1
                self.ingredients[meal]["Cheese"] -= 2
                self.ingredients[meal].pop("Lettuce", None)
            elif meal == "Chicken Soup":
                self.ingredients[meal]["Chicken"] -= 1
                self.ingredients[meal]["Carrots"] -= 1
                self.ingredients[meal]["Celery"] -= 2
                self.ingredients[meal]["Noodles"] -= 1
            
            self.save_inventory()
            print(f"{meal} ordered successfully.")
            return True
        else:
            print("Meal not found!")
            return False
        
