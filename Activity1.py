import tkinter as tk
# Create a window
window = tk.Tk()

window.title('Test')
window.geometry('400x400')
hello = tk.Label(text = "Hello World")
hello.pack()
button = tk.Button(text = "Click me!")
button.pack()
tk.mainloop()

# ACTIVITY DOES NOT RUN ON VSC, OPEN REPLIT TO RUN
