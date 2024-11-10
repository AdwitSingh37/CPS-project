from tkinter import messagebox, simpledialog
import csv


def search_contact():
    search_name = simpledialog.askstring("Search contacts", "Enter the name of the person to search:")
    if search_name:
        flag = False
        with open("contacts.csv",'r') as file:
            line_reader = csv.reader(file)
            next(line_reader)
            for row in line_reader:
                if row[0].lower() == search_name.lower():
                    messagebox.showinfo("Result found", f"Name: {row[0]}\nPhone number: {row[1]}\nAddress: {row[2]}")
                    flag = True
                    break
            if flag == False:
                messagebox.showinfo("Not Found", "No contact found with that name.")