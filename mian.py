class Inventory:
    def __init__(self):
        # Ingredients stock
        self.ingredients = {
            "Steak Dinner": {"Steak": 10, "Potatoes": 20, "Garlic Butter": 5},
            "Salmon Dinner": {"Salmon": 8, "Lemon": 10, "Asparagus": 15},
            "Chicken Alfredo": {"Chicken Breast": 10, "Pasta": 15, "Alfredo Sauce": 8},
            "Burger": {"Buns": 12, "Beef Patty": 10, "Lettuce": 10, "Tomato": 8, "Cheese": 10},
            "Chicken Soup": {"Chicken": 10, "Carrots": 12, "Celery": 10, "Noodles": 15, "Broth": 8}
        }
    
    def view_inventory(self):
      
        """Displays current stock of ingredients."""
        for meal, items in self.ingredients.items():
            print(f"\n{meal}:")
            for ingredient, quantity in items.items():
                print(f"  {ingredient}: {quantity}")
    
    def update_stock(self, meal, ingredient, amount):
        """Updates the stock of a specific ingredient."""
        if meal in self.ingredients and ingredient in self.ingredients[meal]:
            self.ingredients[meal][ingredient] += amount
            print(f"Updated {ingredient} stock for {meal}: {self.ingredients[meal][ingredient]}")
        else:
            print("Invalid meal or ingredient!")
    
    def check_stock(self, meal):
        """Checks the stock for a specific meal."""
        if meal in self.ingredients:
            print(f"\nStock for {meal}:")
            for ingredient, quantity in self.ingredients[meal].items():
                print(f"  {ingredient}: {quantity}")
        else:
            print("Meal not found!")

# Main Program
def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Update Stock")
        print("3. Check Meal Stock")
        print("4. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            inventory.view_inventory()
        elif choice == "2":
            meal = input("Enter meal name: ")
            ingredient = input("Enter ingredient name: ")
            amount = int(input("Enter quantity to add/remove (- for decrease): "))
            inventory.update_stock(meal, ingredient, amount)
        elif choice == "3":
            meal = input("Enter meal name: ")
            inventory.check_stock(meal)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()