'''
Excercise: 

Requirement 1: add one more text label and a button with a function that prints 'Hello'
Requirement 2: the label should say "my label" and be between the entry widget and the buttoon

'''

import tkinter as tk
from tkinter import ttk

def button_func():
  print("a button was pressed")
  
def excercise_button_func():
  print(" Hello ")

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# ttk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master= window)
entry.pack()

''' EXCERCISE SOLUTION '''

excercise_label = ttk.Label(master=window, text='my lable')
excercise_label.pack()

# excercise_button = ttk.Button(master = window, text='excercise button', command = excercise_button_func)
excercise_button = ttk.Button(master = window, text='excercise button', command = lambda: print('hello'))
excercise_button.pack()

# ttk button
button = ttk.Button(master= window, text='A button', command = button_func)
button.pack()

# run
window.mainloop()