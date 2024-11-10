import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os
from collections import Counter
import matplotlib.pyplot as plt

# CSV file to store contacts
csv_file = 'contacts.csv'

# Create CSV file with headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Address"])

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone:")
    address = simpledialog.askstring("Input", "Enter address:")

    if name and phone and address:
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, address])
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to search for a contact by name
def search_contact():
    search_name = simpledialog.askstring("Search", "Enter name to search:")
    if search_name:
        found = False
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[0].lower() == search_name.lower():
                    messagebox.showinfo("Search Result", f"Name: {row[0]}\nPhone: {row[1]}\nAddress: {row[2]}")
                    found = True
                    break
            if not found:
                messagebox.showinfo("Not Found", "No contact found with that name.")

# Function to display all contacts
def display_all_contacts():
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        contacts = [f"Name: {row[0]}, Phone: {row[1]}, Address: {row[2]}" for row in reader]
        
    if contacts:
        print(contacts)
    else:
        messagebox.showinfo("All Contacts", "No contacts available.")

# Function to display digit frequency in phone numbers with Matplotlib
def fun_statistics():
    digit_count = Counter()
    
    # Read the contacts and count digit occurrences in phone numbers
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            phone = row[1]
            digit_count.update(phone)
    
    # Filter only digit keys and ignore non-digit characters
    digit_stats = {str(d): digit_count[str(d)] for d in range(10)}
    digits = list(digit_stats.keys())
    counts = list(digit_stats.values())

    # Custom function to show count and percentage
    def count_and_percentage(pct, all_vals):
        absolute = int(pct/100. * sum(all_vals))
        return f"{absolute} ({pct:.1f}%)"

    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=digits, autopct=lambda pct: count_and_percentage(pct, counts), startangle=140)
    plt.title("Frequency of Each Digit in Phone Numbers")
    plt.show()

# Set up the main Tkinter window
root = tk.Tk()
root.title("Contact Directory")

# Add buttons to the window
btn_add = tk.Button(root, text="Add Contact", command=add_contact, width=20)
btn_add.pack(pady=5)

btn_search = tk.Button(root, text="Search Contact", command=search_contact, width=20)
btn_search.pack(pady=5)

btn_display_all = tk.Button(root, text="Display All Contacts", command=display_all_contacts, width=20)
btn_display_all.pack(pady=5)

btn_statistics = tk.Button(root, text="Fun Statistics", command=fun_statistics, width=20)
btn_statistics.pack(pady=5)

# Run the application
root.mainloop()