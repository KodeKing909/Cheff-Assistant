# Import GUI and system libraries
import tkinter as tk  # Base Tkinter module
from tkinter import messagebox, ttk  # Message popups and ttk widgets (like tabs)
from CheffAssistant import Inventory  # Our custom class for managing inventory and orders
from analytics import get_usage_analytics  # Our custom function to get usage stats
from datetime import datetime, timedelta  # Used for timestamps and weekly logs
import os  # For file handling and folder creation

class OrderGUI:
    """
    This class builds the GUI using Tkinter. It has two tabs:
    1. Order Meals – lets users place meal orders.
    2. Restock & Analytics – lets staff restock ingredients based on usage.
    """
    def __init__(self, root):
        # Set the window title
        self.root = root
        self.root.title("Chef Assistant")

        # Create an Inventory object to track and modify ingredient stock
        self.inventory = Inventory()

        # Create a tab system using ttk.Notebook
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(expand=1, fill="both")  # Stretch the tabs to fill the window

        # === Tab 1: Ordering Meals ===
        self.order_frame = tk.Frame(self.tabs)  # Container (frame) for this tab
        self.tabs.add(self.order_frame, text="Order Meals")  # Add tab to notebook
        self.setup_order_tab()  # Setup layout and widgets for ordering

        # === Tab 2: Restock & Analytics ===
        self.restock_frame = tk.Frame(self.tabs)  # Frame for second tab
        self.tabs.add(self.restock_frame, text="Restock & Analytics")
        self.setup_restock_tab()  # Layout and widgets for restocking

    def setup_order_tab(self):
        """
        This method builds the layout for the Order Meals tab.
        """
        # Label at the top of the order tab
        tk.Label(self.order_frame, text="Select a Meal to Order", font=("Arial", 16)).pack(pady=10)

        # For each meal, create a button to place that order
        for meal in self.inventory.meal_recipes:
            btn = tk.Button(
                self.order_frame,
                text=meal,
                width=30,
                command=lambda m=meal: self.order_meal(m)  # Binds click to ordering function
            )
            btn.pack(pady=3)  # Add vertical spacing

        # === Message Center: Logs and messages ===
        self.message_frame = tk.LabelFrame(self.order_frame, text="Message Center", padx=10, pady=10)
        self.message_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Create a text box to show messages to the user
        self.message_box = tk.Text(self.message_frame, height=8, wrap="word", state="disabled")
        self.message_box.pack(fill="both", expand=True)

    def setup_restock_tab(self):
        """
        Builds the layout for the Restock & Analytics tab.
        Includes a scrollable table with ingredients, analytics, and restock fields.
        """
        # Create a scrollable canvas so the table doesn't overflow
        canvas = tk.Canvas(self.restock_frame)
        scrollbar = ttk.Scrollbar(self.restock_frame, orient="vertical", command=canvas.yview)

        # Frame that sits inside the canvas and holds table rows
        scroll_frame = tk.Frame(canvas)
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")  # Add scroll_frame to canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create column headers at the top of the table
        headers = ["Ingredient", "Weekly Usage", "Stock Left", "Weeks Left", "Suggestion", "Restock Amount", "Action"]
        for col, header in enumerate(headers):
            tk.Label(
                scroll_frame,
                text=header,
                font=("Arial", 10, "bold"),
                borderwidth=1,
                relief="solid",
                padx=5,
                pady=5
            ).grid(row=0, column=col, sticky="nsew")

        # Load the analytics data
        analytics = get_usage_analytics(self.inventory.usage_history, self.inventory.ingredients)

        self.restock_entries = {}  # Dictionary to track entry widgets for restocking input

        # For each ingredient, build a row in the table
        for row, (ingredient, data) in enumerate(analytics.items(), start=1):
            # Ingredient name
            tk.Label(scroll_frame, text=ingredient).grid(row=row, column=0)
            # Weekly usage
            tk.Label(scroll_frame, text=data["weekly_usage"]).grid(row=row, column=1)
            # Current stock
            tk.Label(scroll_frame, text=data["current_stock"]).grid(row=row, column=2)
            # Estimated weeks remaining
            tk.Label(scroll_frame, text=data["weeks_remaining"]).grid(row=row, column=3)
            # Suggested restock amount
            tk.Label(scroll_frame, text=data["restock_suggestion"]).grid(row=row, column=4)

            # Entry box to input restock quantity
            entry = tk.Entry(scroll_frame, width=10)
            entry.grid(row=row, column=5)
            self.restock_entries[ingredient] = entry  # Store reference to entry widget

            # Restock button for each row
            button = tk.Button(
                scroll_frame,
                text="Restock",
                command=lambda i=ingredient: self.restock_ingredient_gui(i)
            )
            button.grid(row=row, column=6)

    def restock_ingredient_gui(self, ingredient):
        """
        Called when staff clicks a restock button in the GUI.
        Reads the amount from entry and updates the inventory.
        """
        # Get Entry widget for the specified ingredient
        entry = self.restock_entries[ingredient]
        try:
            amount = int(entry.get())
            if amount > 0:
                # Restock the ingredient in the inventory system
                self.inventory.restock_ingredient(ingredient, amount)

                # Show confirmation popup for the user
                messagebox.showinfo("Restocked", f"{ingredient} restocked by {amount}")

                # Refresh the tab so new stock levels are shown
                self.refresh_restock_tab()

            else:
                messagebox.showwarning("Invalid Input", "Enter a positive number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def refresh_restock_tab(self):
        """
        Clears and reloads the Restock & Analytics tab to reflect updated values.
        """
        for widget in self.restock_frame.winfo_children():
            widget.destroy()  # Clear old widgets
        self.setup_restock_tab()  # Rebuild with updated data

    def log_message(self, message):
        """
        Adds a timestamped message to the message box and saves to log file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dated_message = f"[{timestamp}] {message}"

        # Add to message box in GUI
        self.message_box.configure(state="normal")
        self.message_box.insert(tk.END, dated_message + "\n")
        self.message_box.configure(state="disabled")
        self.message_box.see(tk.END)

        # Save to log file grouped by week
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
        """
        Writes a snapshot of the current inventory to the log file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        snapshot_header = f"[{timestamp}] 📦 Inventory Snapshot:"
        inventory_lines = [f"    {ingredient}: {amount}" for ingredient, amount in self.inventory.ingredients.items()]
        snapshot = "\n".join([snapshot_header] + inventory_lines)

        # Write to the same weekly log file
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        now = datetime.now()
        start_of_week = now - timedelta(days=now.weekday())
        week_str = start_of_week.strftime("%Y-%m-%d")
        log_filename = f"week-{week_str}.log"
        log_path = os.path.join(log_dir, log_filename)

        with open(log_path, "a") as log_file:
            log_file.write(snapshot + "\n")

        # Also show in GUI message box
        self.message_box.configure(state="normal")
        self.message_box.insert(tk.END, snapshot + "\n")
        self.message_box.configure(state="disabled")
        self.message_box.see(tk.END)

    def order_meal(self, meal):
        """
        Triggered when a meal button is clicked.
        Checks stock, logs messages, places order, and shows result.
        """
        recipe = self.inventory.meal_recipes[meal]
        max_possible = float('inf')
        for ingredient, amount_needed in recipe.items():
            available = self.inventory.ingredients.get(ingredient, 0)
            possible = available // amount_needed if amount_needed > 0 else 0
            max_possible = min(max_possible, possible)

        if max_possible <= 5:
            warning = f"⚠️ CRITICAL: Stock low for '{meal}' — only {max_possible} can be made."
            self.log_message(warning)
            self.log_inventory_snapshot()
            messagebox.showwarning("Critical Inventory Warning", warning)
        else:
            self.log_message(f"Attempting to order {meal}...")

        success = self.inventory.place_order(meal)
        if success:
            confirmation = f"✅ Order placed: {meal}"
            self.log_message(confirmation)
        else:
            error = f"❌ Failed to place order: Not enough ingredients for {meal}"
            self.log_message(error)
            messagebox.showerror("Insufficient Ingredients", error)

# ==== Start the GUI ====
if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
