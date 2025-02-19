class Inventory:
    def __init__(self):
        # Dictionary to hold Meals and their ingredients. Only included main ingredients as of now.
        self.ingredients = {
            "Steak Dinner": {"Steak": 10, "Potatoes": 20, "Garlic Butter": 5},
            "Salmon Dinner": {"Salmon": 8, "Lemon": 10, "Asparagus": 15},
            "Chicken Alfredo": {"Chicken Breast": 10, "Pasta": 15, "Alfredo Sauce": 8},
            "Burger": {"Buns": 12, "Beef Patty": 10, "Lettuce": 10, "Tomato": 8, "Cheese": 10},
            "Chicken Soup": {"Chicken": 10, "Carrots": 12, "Celery": 10, "Noodles": 15, "Broth": 8}
        }
        # Usage history kept here for weekly averaging
        self.usage_history = {ingredient: [] for meal in self.ingredients for ingredient in self.ingredients [meal]}
    
    def view_inventory(self):
      
        #Displays current stock of ingredients.
        for meal, items in self.ingredients.items():
            print(f"\n{meal}:")
            for ingredient, quantity in items.items():
                print(f"  {ingredient}: {quantity}")
    
    def update_stock(self, meal, ingredient, amount):
        #Updates the stock of a specific ingredient.
        if meal in self.ingredients and ingredient in self.ingredients[meal]:
            self.ingredients[meal][ingredient] += amount
            print(f"Updated {ingredient} stock for {meal}: {self.ingredients[meal][ingredient]}")
        else:
            print("Invalid meal or ingredient!")
    
    def check_stock(self, meal):
        #Checks the stock for a specific meal.
        if meal in self.ingredients:
            print(f"\nStock for {meal}:")
            for ingredient, quantity in self.ingredients[meal].items():
                print(f"  {ingredient}: {quantity}")
        else:
            print("Meal not found!")

    def place_order (self, meal):
        # Deducts ingredients fro inventory and records usage when an order is placed.
        if meal in self.ingredients:
            required_ingredients = self.ingredients[meal]

            # Checks if there is enough ingredients/inventory (requires at least 1 per order)
            for ingredient in required_ingredients:
                if self.ingredients[meal][ingredient] < 1:
                    print (f"Not enough {ingredient} to make {meal}. Restock needed.")
                    return False
                
            # Deducts 1 unit per ingredient and records history
            for ingredient in required_ingredients:
                self.ingredients[meal][ingredient] -= 1
                self.usage_history[ingredient].append(1) # Record 1 unit used

            print (f" {meal}  ordered successfully.")
            return True
        else: 
            print("Meal not found!")
            return False

# Main Program
def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Update Stock")
        print("3. Check Meal Stock")
        print("4. Exit")
        print("5. Place Order")
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
            break           #Exits the loop and terminates the program.
        elif choice == "5":
            meal = input("Enter the meal name you want to order:")
            order_success = inventory.place_order(meal)
            if order_success:
                print(f"The order for {meal} has been placed successfully.")
            else:
                print(f"Failed to place the order for {meal}.")
        else:
            print(f"Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
