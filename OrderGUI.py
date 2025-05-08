
import tkinter as tk
from tkinter import messagebox, ttk
from CheffAssistant import Inventory
from analytics import get_usage_analytics
from datetime import datetime, timedelta
import os
import sys
from PIL import Image, ImageTk

class OrderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chef Assistant")

        self.inventory = Inventory()

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(expand=1, fill="both")

        self.order_frame = tk.Frame(self.tabs)
        self.tabs.add(self.order_frame, text="Order Meals")
        self.setup_order_tab()

        self.restock_frame = tk.Frame(self.tabs)
        self.tabs.add(self.restock_frame, text="Restock & Analytics")
        self.setup_restock_tab()

    def resource_path(self, relative_path):
        # Handles image path resolution for both development and PyInstaller executable
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def setup_order_tab(self):
        # Title for the order tab
        tk.Label(self.order_frame, text="Tap an Image to Order a Meal", font=("Arial", 16)).pack(pady=10)

        self.image_refs = {}

        # A frame to hold all meal buttons
        grid_frame = tk.Frame(self.order_frame)
        grid_frame.pack(pady=10)

        col_count = 3
        row = 0
        col = 0

        for meal in self.inventory.meal_recipes:
            image_path = self.resource_path(f"images/{meal}.png")
            if os.path.exists(image_path):
                img = Image.open(image_path).resize((150, 110))
                photo = ImageTk.PhotoImage(img)
                self.image_refs[meal] = photo

                # Create a container for the image and label
                container = tk.Frame(grid_frame, padx=10, pady=10)
                container.grid(row=row, column=col)

                # Image as a clickable button
                btn = tk.Button(container, image=photo, command=lambda m=meal: self.order_meal(m))
                btn.pack()

                # Label underneath the image
                tk.Label(container, text=meal).pack(pady=4)

                col += 1
                if col >= col_count:
                    col = 0
                    row += 1
            else:
                print(f"Missing image for meal: {meal}")

        self.message_frame = tk.LabelFrame(self.order_frame, text="Message Center", padx=10, pady=10)
        self.message_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.message_box = tk.Text(self.message_frame, height=8, wrap="word", state="disabled")
        self.message_box.pack(fill="both", expand=True)

    def setup_restock_tab(self):
        canvas = tk.Canvas(self.restock_frame)
        scrollbar = ttk.Scrollbar(self.restock_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        headers = ["Ingredient", "Weekly Usage", "Stock Left", "Weeks Left", "Suggestion", "Restock Amount", "Action"]
        for col, header in enumerate(headers):
            tk.Label(scroll_frame, text=header, font=("Arial", 10, "bold"), borderwidth=1,
                     relief="solid", padx=5, pady=5).grid(row=0, column=col, sticky="nsew")

        analytics = get_usage_analytics(self.inventory.usage_history, self.inventory.ingredients)
        self.restock_entries = {}

        for row, (ingredient, data) in enumerate(analytics.items(), start=1):
            tk.Label(scroll_frame, text=ingredient).grid(row=row, column=0)
            tk.Label(scroll_frame, text=data["weekly_usage"]).grid(row=row, column=1)
            tk.Label(scroll_frame, text=data["current_stock"]).grid(row=row, column=2)
            tk.Label(scroll_frame, text=data["weeks_remaining"]).grid(row=row, column=3)
            tk.Label(scroll_frame, text=data["restock_suggestion"]).grid(row=row, column=4)

            entry = tk.Entry(scroll_frame, width=10)
            entry.grid(row=row, column=5)
            self.restock_entries[ingredient] = entry

            button = tk.Button(
                scroll_frame,
                text="Restock",
                command=lambda i=ingredient: self.restock_ingredient_gui(i)
            )
            button.grid(row=row, column=6)

    def restock_ingredient_gui(self, ingredient):
        entry = self.restock_entries[ingredient]
        try:
            amount = int(entry.get())
            if amount > 0:
                self.inventory.restock_ingredient(ingredient, amount)
                messagebox.showinfo("Restocked", f"{ingredient} restocked by {amount}")
                self.refresh_restock_tab()
            else:
                messagebox.showwarning("Invalid Input", "Enter a positive number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def refresh_restock_tab(self):
        for widget in self.restock_frame.winfo_children():
            widget.destroy()
        self.setup_restock_tab()

    def log_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dated_message = f"[{timestamp}] {message}"
        self.message_box.configure(state="normal")
        self.message_box.insert(tk.END, dated_message + "\n")
        self.message_box.configure(state="disabled")
        self.message_box.see(tk.END)

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        now = datetime.now()
        start_of_week = now - timedelta(days=now.weekday())
        week_str = start_of_week.strftime("%Y-%m-%d")
        log_filename = f"week-{week_str}.log"
        log_path = os.path.join(log_dir, log_filename)
        with open(log_path, "a") as log_file:
            log_file.write(dated_message + "\n")

    def log_inventory_snapshot(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        snapshot_header = f"[{timestamp}] Inventory Snapshot:"
        inventory_lines = [f"    {ingredient}: {amount}" for ingredient, amount in self.inventory.ingredients.items()]
        snapshot = "\n".join([snapshot_header] + inventory_lines)

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        now = datetime.now()
        start_of_week = now - timedelta(days=now.weekday())
        week_str = start_of_week.strftime("%Y-%m-%d")
        log_filename = f"week-{week_str}.log"
        log_path = os.path.join(log_dir, log_filename)
        with open(log_path, "a") as log_file:
            log_file.write(snapshot + "\n")

        self.message_box.configure(state="normal")
        self.message_box.insert(tk.END, snapshot + "\n")
        self.message_box.configure(state="disabled")
        self.message_box.see(tk.END)

    def order_meal(self, meal):
        recipe = self.inventory.meal_recipes[meal]
        max_possible = float('inf')
        for ingredient, amount_needed in recipe.items():
            available = self.inventory.ingredients.get(ingredient, 0)
            possible = available // amount_needed if amount_needed > 0 else 0
            max_possible = min(max_possible, possible)

        if max_possible <= 5:
            warning = f"CRITICAL: Stock low for '{meal}' — only {max_possible} can be made."
            self.log_message(warning)
            self.log_inventory_snapshot()
            messagebox.showwarning("Critical Inventory Warning", warning)
        else:
            self.log_message(f"Attempting to order {meal}...")

        success = self.inventory.place_order(meal)
        if success:
            confirmation = f"Order placed: {meal}"
            self.log_message(confirmation)
        else:
            error = f"Failed to place order: Not enough ingredients for {meal}"
            self.log_message(error)
            messagebox.showerror("Insufficient Ingredients", error)

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
