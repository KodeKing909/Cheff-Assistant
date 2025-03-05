import tkinter as tk
from tkinter import messagebox
from CheffAssistant import Inventory

# Initialize inventory
inventory = Inventory()

# Update stock function
def update_stock(meal, ingredient, amount):
    result = inventory.update_stock(meal, ingredient, amount)
    messagebox.showinfo("Update Stock", result)
    refresh_inventory()

# Place an order
def place_order(meal):
    result = inventory.place_order(meal)
    messagebox.showinfo("Order", result)
    refresh_inventory()

# Refresh the inventory display
def refresh_inventory():
    for widget in frame_inventory.winfo_children():
        widget.destroy()

    for meal, ingredients in inventory.ingredients.items():
        meal_label = tk.Label(frame_inventory, text=meal, font=("Arial", 12, "bold"))
        meal_label.pack()

        for ingredient, qty in ingredients.items():
            row = tk.Frame(frame_inventory)
            row.pack(pady=2)
            tk.Label(row, text=f"{ingredient}: {qty}").pack(side="left")
            tk.Button(row, text="+", command=lambda m=meal, i=ingredient: update_stock(m, i, 1)).pack(side="left")
            tk.Button(row, text="-", command=lambda m=meal, i=ingredient: update_stock(m, i, -1)).pack(side="left")

        tk.Button(frame_inventory, text=f"Order {meal}", command=lambda m=meal: place_order(m)).pack(pady=5)

# Tkinter window setup
root = tk.Tk()
root.title("Cheff Assistant Inventory")
root.geometry("400x500")

tk.Label(root, text="Inventory Management", font=("Arial", 16, "bold")).pack(pady=10)

frame_inventory = tk.Frame(root)
frame_inventory.pack(pady=10, fill="both", expand=True)

refresh_inventory()

root.mainloop()

