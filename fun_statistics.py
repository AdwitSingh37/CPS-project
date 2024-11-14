import csv
import matplotlib.pyplot as plt
def fun_statistics():
    # Initialize counts for each digit (0 through 9)
    digit_counts = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    
    # Read the contacts and count digit occurrences in phone numbers
    with open("contacts.csv",'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            for i in row[1]:
                if i.isdigit():  
                    digit_counts[i] += 1

    digits = list(digit_counts.keys()) #data for the bar graph
    counts = list(digit_counts.values())
    
    # Create a bar chart
    plt.figure(figsize=(8, 6)) #size of the bar chart window(width,height)
    plt.bar(digits, counts, color='indigo')#x axis, y axis and colour
    plt.xlabel("Digits")
    plt.ylabel("Frequency")
    plt.title("Frequency of Each Digit in Phone Numbers")
    plt.show() #shows the final chart on the screen
