#Importing
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox


# Function to add a new contact
def add_contact():
	name = simpledialog.askstring("Input", "Enter name:") 
	phone = simpledialog.askstring("Input", "Enter phone:") 
	if len(phone)!=10:  #if 10 numbers are not available ask user to type again
		messagebox.showwarning("Input Error", "Please enter valid phone number.")
		phone = simpledialog.askstring("Input", "Enter phone:")
	address=simpledialog.askstring("Input", "Enter address:")
	

	if name and phone and address:
		with open(csv_file, mode='a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([name, phone, address])
		messagebox.showinfo("Success", "Contact added successfully!")
	elif( name and phone and not address): #if the user doesn't type address 
		with open ("contacts.csv",'a',newline='') as file:
			writer=csv.writer(file)
			writer.writerow([name,phone,"Nil"])
		messagebox.showinfo("Contact add","Contact added sucessfully without address!")
	else:  #if the user doesn't fill feilds other than address
		messagebox.showwarning("Input Error", "Please fill in all fields.")
