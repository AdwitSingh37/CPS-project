from tkinter import messagebox, simpledialog
import csv


def remove_contact():
    remove_name = simpledialog.askstring("Search contacts", "Enter the name of the person to remove:")
    if remove_name:
        lines = list()
        flag = 0
        with open('contacts.csv', 'r') as file:
            
            reader = csv.reader(file)
            
            for row in reader:
                lines.append(row)
                if row[0].lower() == remove_name.lower():
                    lines.remove(row)
                    flag = 1
        if flag == 1:
            with open('contacts.csv', 'w',newline='\n') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            messagebox.showinfo("Removed", "Contact is removed.")
        else:
            messagebox.showinfo("Error","Contact does not exist")
