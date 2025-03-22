import tkinter as tk
from tkinter import messagebox
from CheffAssistant import Inventory

class OrderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chef Assistant - Order Meals")
        self.inventory = Inventory()

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.title_label = tk.Label(self.frame, text="Select a Meal to Order", font=("Arial", 16))
        self.title_label.pack(pady=10)

        for meal in self.inventory.meal_recipes:
            btn = tk.Button(self.frame, text=meal, width=30, command=lambda m=meal: self.order_meal(m))
            btn.pack(pady=3)

        self.stock_label = tk.Label(self.frame, text="", justify="left")
        self.stock_label.pack(pady=10)

        self.refresh_inventory()

    def order_meal(self, meal):
        success = self.inventory.place_order(meal)
        if success:
            messagebox.showinfo("Order Placed", f"Successfully ordered {meal}!")
        else:
            messagebox.showerror("Insufficient Ingredients", f"Not enough ingredients for {meal}.")
        self.refresh_inventory()

    def refresh_inventory(self):
        display_text = "Current Inventory:\n"
        for ingredient, amount in self.inventory.ingredients.items():
            display_text += f"{ingredient}: {amount}\n"
        self.stock_label.config(text=display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
