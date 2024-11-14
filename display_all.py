from tkinter import messagebox
import csv
def display_all_contacts():
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file) #reader is the variable which now holds all the data of the csv file
        next(reader)  #this skips the first row which represents the title for each column
        contacts = [f"Name: {row[0]}, Phone: {row[1]}, Address: {row[2]}" for row in reader] #list comprehension is used here. "row" takes one row of the csv file at a time
        
    if contacts: #checks if atleast one contact is entered by the user
        for contact in contacts: #traverses through each contact row in the file and later print it
            print(contact)
    else:
        messagebox.showinfo("All Contacts", "No contacts available.")
