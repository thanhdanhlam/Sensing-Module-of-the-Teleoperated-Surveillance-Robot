from tkinter import *
from tkinter import ttk

# Create instance of Tkinter frame
root = Tk()

# Set geometry for frame
root.geometry('750x250')

def display_text():
    global entry
    string = entry.get()
    Label.configure(text=string)

# Initialize a Label to display User Input
label=Label(root, text="", font=("Arial 20 bold"))
label.pack()

#frm = ttk.Frame(root, padding=10)
#frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit",command=root.destroy).grid(column=0, row=1)

# Create an Entry widget to accept User Input
entry = Entry(root, width=40)
entry.focus_set()
entry.pack()

# Create Button to validate Entry Widget
ttk.Button(root, text="Okay", width=20, command=display_text).pack(pady=15)

root.mainloop()

