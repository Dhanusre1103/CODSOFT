import tkinter as tk
import random
import string
from tkinter import messagebox
def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Ensure at least one character from each set is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)
def generate_password_gui():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return

        password = generate_password(length)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.pack(pady=10)

result_entry = tk.Entry(root, width=30)
result_entry.pack(pady=10)

# Run the main loop
root.mainloop()
