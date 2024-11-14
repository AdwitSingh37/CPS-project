from tkinter import messagebox
import csv
def display_all_contacts():
    with open('contacts.csv','r') as file:
        reader = csv.reader(file) #reader is the variable which now holds all the data of the csv file
        next(reader)  
        contacts = [f"Name: {row[0]}, Phone: {row[1]}, Address: {row[2]}" for row in reader] #list comprehension is used here. Formats the string and stores the data into a list
        print(contacts)
    if contacts: #checks if atleast one contact is entered by the user
        for contact in contacts: #traverses through each contact row in the file and later print it
            print(contact)
    else:
        messagebox.showinfo("All Contacts", "No contacts available.")
