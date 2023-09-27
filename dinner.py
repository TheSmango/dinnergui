import tkinter as tk
from tkinter import ttk
import random

# List of restaurant choices
restaurant_data = [
    "McDonald's", "Wendy's", "Mi Hacienda", "Applebee's", "Bob Evans",
    "Red Robin", "Cracker Barrel", "Texas Steakhouse", "Chinese", "Golden Corral",
    "Dairy Queen", "Lee's Chicken", "Taco Bell", "Subway", "Farmhouse Diner",
    "1 2 3 Food Court", "Arbys", "Hardee's", "KFC", "Little Caesars",
    "Billy Ray's", "The Brickhouse", "El Dorado", "Giovanni's", "Pig in a Poke",
    "Fazoli's", "Long John Silver's", "Buffalo Wild Wings",
]


# Function to choose a random restaurant and display it with a message
def choose_random_restaurant():
    chosen_restaurant.set("")

    # Animate restaurant names
    animate_restaurant_names()


# Function to animate restaurant names
def animate_restaurant_names():
    chosen = random.choice(restaurant_data)
    chosen_restaurant.set("Looks like you are eating at:\n" + chosen)


# Create the main window
window = tk.Tk()
window.geometry("500x1200")
window.title("Restaurant Randomizer")

# Create a button
random_button = tk.Button(window, text="Randomly Select", command=choose_random_restaurant)
random_button.pack()

# Create a label to display the chosen restaurant
chosen_restaurant = tk.StringVar()
result_label = tk.Label(window, textvariable=chosen_restaurant, font=("Helvetica", 24))
result_label.pack()

# Create a scrolled list to display restaurant names
listbox_frame = ttk.Frame(window)
listbox_frame.pack(fill=tk.BOTH, expand=True)

restaurant_listbox = tk.Listbox(listbox_frame, font=("Helvetica", 18), selectmode=tk.SINGLE)
restaurant_listbox.pack(fill=tk.BOTH, expand=True)

for restaurant in restaurant_data:
    restaurant_listbox.insert(tk.END, restaurant)

# Start the GUI event loop
window.mainloop()
