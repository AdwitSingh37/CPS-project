#Importing
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

# CSV file to store contacts
csv_file = 'contacts.csv'

# Function to add a new contact
def add_contact():
	name = simpledialog.askstring("Input", "Enter name:")
	phone = simpledialog.askstring("Input", "Enter phone:")
	if len(phone)!=10:
		messagebox.showwarning("Input Error", "Please enter valid phone number.")
		phone = simpledialog.askstring("Input", "Enter phone:")
	address=simpledialog.askstring("Input", "Enter address:")
	

	if name and phone and address:
		with open(csv_file, mode='a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([name, phone, address])
		messagebox.showinfo("Success", "Contact added successfully!")
	elif( name and phone and not address):
		with open ("contacts.csv",'a',newline='') as file:
			writer=csv.writer(file)
			writer.writerow([name,phone,"Nil"])
		messagebox.showinfo("Contact add","Contact added sucessfully without address!")
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
