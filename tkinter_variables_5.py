'''
Tkinter has inbuilt variables that are designed to work well with widgets

that is they are automatically udpated by a widget & they update a widget

Although they still store basic data like string, integers & Booleans

'''

# Task/Project:  
# Label should always have the same text of Entry -- i.e. as we change the text in entry lable text
# should keep changing real time

# How it works ?
# Entry -----AUTOMATIC GETTING----> StringVar -----AUTOMATIC SETTING----> Label
# The 2 widgets Entry & Label are closely connected through ---> StringVar

import tkinter as tk
from tkinter import ttk

def button_func():
  print(string_var.get())
  string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('300x100')

# tkinter variable
string_var = tk.StringVar()

# widgets 

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

# run
window.mainloop()


