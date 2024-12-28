from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title("Multiplication Application")
root.geometry("400x300")

# Add widgets
# Add Label
lbl = Label(text="Enter Two Numbers to Multiply", fg="white", bg="#072F5F", height=1, width=300)

# Add Labels and Entry Widgets for Two Numbers
num1_lbl = Label(text="Number 1:", bg="#3895D3")
num1_entry = Entry()

num2_lbl = Label(text="Number 2:", bg="#3895D3")
num2_entry = Entry()

# Function to Calculate and Display Product
def display():
    try:
        # Get input numbers
        num1 = float(num1_entry.get())

        num2 = float(num2_entry.get())
        # Calculate product
        product = num1 * num2

        # Display details in a text box
        text_box.delete("1.0", END)  # Clear previous content

        message = "Welcome to the Multiplication App!\nToday's date is: " + str(date.today()) + "\n"
        result = "The product of {} and {} is: {}\n".format(num1, num2, product)

        text_box.insert(END, message)
        text_box.insert(END, result)

    except ValueError:
        text_box.delete("1.0", END)
        text_box.insert(END, "Error: Please enter valid numbers.")

# Add a Text Widget to display information/messages
text_box = Text(height=5)

# Add Button
btn = Button(text="Calculate", command=display, height=1, bg="#1261A0", fg="white")

# Organize all the widgets in the window
lbl.pack()
num1_lbl.pack()
num1_entry.pack()
num2_lbl.pack()
num2_entry.pack()
btn.pack()
text_box.pack()

# Run the application
root.mainloop()

# ACTIVITY DOES NOT RUN ON VSC, OPEN REPLIT > TKINTER TO RUN

