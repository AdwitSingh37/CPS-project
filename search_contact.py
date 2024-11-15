from tkinter import messagebox, simpledialog # Import modules for dialogs and message boxes
import csv # Import the CSV module for reading and working with CSV files


def search_contact():
    # Prompt the user to enter the name of the person they want to search for
    search_name = simpledialog.askstring("Search contacts", "Enter the name of the person to search:")
    # Check if the user entered a name; if not, exit the function
    if search_name:
        flag = False # Initialize a flag to indicate if a contact is found
        # Open the CSV file in read mode
        with open("contacts.csv",'r') as file:
            line_reader = csv.reader(file) # Create a CSV reader to read lines in the CSV file
            next(line_reader)  # Skip the header row (assumes there is a header row)

            # Loop through each row in the CSV file
            for row in line_reader:
                # Check if the first column (name) matches the search term (case-insensitive)
                if row[0].lower() == search_name.lower():
                     # Display contact information if a match is found
                    messagebox.showinfo("Result found", f"Name: {row[0]}\nPhone number: {row[1]}\nAddress: {row[2]}")
                    flag = True # Set the flag to True to indicate a match was found
                    break
            # If the flag is still False, no contact was found
            if flag == False:
                messagebox.showinfo("Not Found", "No contact found with that name.")
