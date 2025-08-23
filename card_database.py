import tkinter as tk
from tkinter import messagebox
import os

# File path for the database
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
database_file = os.path.join(desktop_path, "cards_list.txt")

# Ensure the file exists
if not os.path.exists(database_file):
    with open(database_file, "w") as f:
        f.write("")

# Function to center a window on the screen
def center_window(window, width=None, height=None):
    """
    Centers a tkinter window on the screen.
    Optionally, you can set the width and height of the window.
    """
    window.update_idletasks()  # Ensure correct window size is calculated
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Use the window's current size if width and height aren't provided
    window_width = width if width else window.winfo_width()
    window_height = height if height else window.winfo_height()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Main menu function
def main_menu():
    def new_entry():
        root.destroy()
        new_entry_window()

    def lookup():
        root.destroy()
        lookup_window()

    def exit_program():
        root.destroy()

    root = tk.Tk()
    root.title("Pokemon Card Database")
    root.geometry("400x300")
    center_window(root)  # Center the window

    tk.Button(root, text="New Entry", command=new_entry, width=20, font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=20)
    tk.Button(root, text="Look up Pokemon", command=lookup, width=20, font=("Arial", 12, "bold"), bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="EXIT", command=exit_program, width=20, font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=20)

    root.mainloop()

# New entry window
def new_entry_window():
    def save_to_database():
        year = year_entry.get()
        card_number = card_number_entry.get()
        card_name = card_name_entry.get()
        set_name = set_name_entry.get()
        condition = condition_entry.get()
        tags = tags_entry.get()

        if not all([year, card_number, card_name, set_name, condition, tags]):
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return

        # Save the data to the database in a horizontal format
        with open(database_file, "a") as f:
            f.write(
                f"Year: {year}  "
                f"Card Number: {card_number}  "
                f"Card Name: {card_name}  "
                f"Set Name: {set_name}  "
                f"Condition: {condition}  "
                f"Tags: {tags}\n"
            )

        messagebox.showinfo("Success", "Card saved successfully!")
        entry_window.destroy()
        main_menu()

    def cancel():
        entry_window.destroy()
        main_menu()

    entry_window = tk.Tk()
    entry_window.title("New Entry")
    entry_window.geometry("500x500")
    center_window(entry_window)  # Center the window

    tk.Label(entry_window, text="Year of Release:", font=("Arial", 12, "bold")).pack(pady=5)
    year_entry = tk.Entry(entry_window, width=40, justify="center")
    year_entry.pack()

    tk.Label(entry_window, text="Card Number:", font=("Arial", 12, "bold")).pack(pady=5)
    card_number_entry = tk.Entry(entry_window, width=40, justify="center")
    card_number_entry.pack()

    tk.Label(entry_window, text="Card Name:", font=("Arial", 12, "bold")).pack(pady=5)
    card_name_entry = tk.Entry(entry_window, width=40, justify="center")
    card_name_entry.pack()

    tk.Label(entry_window, text="Set Name:", font=("Arial", 12, "bold")).pack(pady=5)
    set_name_entry = tk.Entry(entry_window, width=40, justify="center")
    set_name_entry.pack()

    tk.Label(entry_window, text="Condition:", font=("Arial", 12, "bold")).pack(pady=5)
    condition_entry = tk.Entry(entry_window, width=40, justify="center")
    condition_entry.pack()

    tk.Label(entry_window, text="Tags (comma-separated):", font=("Arial", 12, "bold")).pack(pady=5)
    tags_entry = tk.Entry(entry_window, width=40, justify="center")
    tags_entry.pack()

    tk.Button(entry_window, text="Save to Database", command=save_to_database, width=20, font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(entry_window, text="Cancel", command=cancel, width=20, font=("Arial", 12, "bold")).pack()

    entry_window.mainloop()

# Edit card window
def edit_card_window(card_data):
    def save_changes():
        new_data = edit_text.get("1.0", tk.END).strip()
        with open(database_file, "r") as f:
            all_data = f.readlines()

        # Replace the old entry with the new one
        for i in range(len(all_data)):
            if all_data[i].strip() == card_data.strip():
                all_data[i] = new_data + "\n"
                break

        with open(database_file, "w") as f:
            f.writelines(all_data)

        messagebox.showinfo("Success", "Card updated successfully!")
        edit_window.destroy()
        main_menu()

    def cancel():
        edit_window.destroy()
        main_menu()

    edit_window = tk.Tk()
    edit_window.title("Edit Card")
    edit_window.geometry("700x400")
    center_window(edit_window)

    tk.Label(edit_window, text="Edit Card Details", font=("Arial", 12, "bold")).pack(pady=10)
    edit_text = tk.Text(edit_window, width=80, height=15, font=("Arial", 10), bg="yellow", fg="black")
    edit_text.insert(tk.END, card_data)
    edit_text.pack(pady=10)

    tk.Button(edit_window, text="Save Changes", command=save_changes, width=20, font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=5)
    tk.Button(edit_window, text="Cancel", command=cancel, width=20, font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=5)

    edit_window.mainloop()

# Lookup window
def lookup_window():
    def search_by(criteria):
        search_window.destroy()
        input_search_window(criteria)

    def back_to_main():
        search_window.destroy()
        main_menu()

    search_window = tk.Tk()
    search_window.title("Look Up Pokemon")
    search_window.geometry("400x300")
    center_window(search_window)  # Center the window

    tk.Label(search_window, text="Search by:", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Button(search_window, text="Tags", command=lambda: search_by("Tags"), width=20, font=("Arial", 12, "bold"), bg="red", fg="black").pack(pady=5)
    tk.Button(search_window, text="Card Number", command=lambda: search_by("Card Number"), width=20, font=("Arial", 12, "bold"), bg="white", fg="black").pack(pady=5)
    tk.Button(search_window, text="Name", command=lambda: search_by("Name"), width=20, font=("Arial", 12, "bold"), bg="blue", fg="white").pack(pady=5)
    tk.Button(search_window, text="Cancel", command=back_to_main, width=20, font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)

    search_window.mainloop()

# Input search window
def input_search_window(criteria):
    def perform_search():
        query = search_entry.get().strip()
        if not query:
            messagebox.showwarning("Missing Input", "Please enter a search term.")
            return

        input_window.destroy()
        search_results_window(criteria, query)

    def cancel():
        input_window.destroy()
        lookup_window()

    input_window = tk.Tk()
    input_window.title(f"Search by {criteria}")
    input_window.geometry("400x200")
    center_window(input_window)  # Center the window

    tk.Label(input_window, text=f"Enter {criteria}:", font=("Arial", 12, "bold")).pack(pady=10)
    search_entry = tk.Entry(input_window, width=40, justify="center")
    search_entry.pack(pady=5)

    tk.Button(input_window, text="Search", command=perform_search, width=15, font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=5)
    tk.Button(input_window, text="Cancel", command=cancel, width=15, font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=5)

    input_window.mainloop()

# Search results window
def search_results_window(criteria, query):
    def load_card(card_data):
        results_window.destroy()
        edit_card_window(card_data)

    def back_to_lookup():
        results_window.destroy()
        lookup_window()

    results_window = tk.Tk()
    results_window.title("Search Results")
    results_window.geometry("1000x800")
    center_window(results_window)  # Center the window

    tk.Label(results_window, text=f"Search Results for {criteria}: {query}", font=("Arial", 12, "bold")).pack(pady=10)

    # Perform the search
    results = []
    with open(database_file, "r") as f:
        # Each row is treated as a separate entry
        cards = f.readlines()
        for card in cards:
            if query.lower() in card.lower():  # Match the query case-insensitively
                results.append(card.strip())  # Add the card entry (strip removes extra spaces/newlines)

    if results:
        frame = tk.Frame(results_window)
        frame.pack(pady=10)

        for index, card in enumerate(results):
            card_button = tk.Button(
                frame,
                text=card,  # Show the card details as a single line
                command=lambda c=card: load_card(c),  # Pass the full card entry to load_card
                font=("Arial", 10),
                width=80,  # Adjust button width to fit long text
                anchor="w",  # Align text to the left
                wraplength=600  # Prevent text wrapping
            )
            card_button.pack(pady=5, padx=10, fill="x")  # Stretch the button to fit the frame
    else:
        tk.Label(results_window, text="No results found.", font=("Arial", 12, "bold")).pack(pady=10)

    tk.Button(results_window, text="Back", command=back_to_lookup, width=20, font=("Arial", 12, "bold"), bg="black", fg="white").pack(pady=10)

    results_window.mainloop()
# Lookup window and search functionality remain unchanged

# Start the program
main_menu()
