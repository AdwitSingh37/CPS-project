import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os
from add_contact import add_contact
from fun_statistics import fun_statistics
from search_contact import search_contact
from display_all import display_all_contacts
from remove_contact import remove_contact

# Create CSV file with headers if it doesn't exist
if not os.path.exists('contacts.csv'):
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Address"])


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

btn_statistics = tk.Button(root, text="Remove Contact", command=remove_contact, width=20)
btn_statistics.pack(pady=5)

btn_statistics = tk.Button(root, text="Fun Statistics", command=fun_statistics, width=20)
btn_statistics.pack(pady=5)

# Run the application
root.mainloop()
