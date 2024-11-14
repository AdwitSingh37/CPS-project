from tkinter import messagebox
import csv
def display_all_contacts():
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        contacts = [f"Name: {row[0]}, Phone: {row[1]}, Address: {row[2]}" for row in reader]
        
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        messagebox.showinfo("All Contacts", "No contacts available.")
