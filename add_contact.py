#Importing
import csv
from tkinter import simpledialog, messagebox

# Function to add a new contact 
def add_contacts():
    name=simpledialog.askstring("Input","Enter name:")
    phone=simpledialog.askstring("Input","Enter phone number:")
    address=simpledialog.askstring("Input","Enter address:")

    if name and phone and address:
        with open ("contacts.csv",'a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([name,phone,address])
        messagebox.showinfo("Contact added sucessfully!")
    else:
        messagebox.showwarning("Input error", "Please fill in all the feilds")
