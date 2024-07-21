'''
Create 2 entry fields and 1 label. They should all be connected via a StringVar
Set a start value of 'test'
'''

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tkinter Variables Excercise')
window.geometry('500x300')

# tkinter variable
string_var = tk.StringVar(value='test')   # start value set to 'test'
'''
Another way to set start value --->   string_var.set('test')

'''

# widgets

entry1 = ttk.Entry(master=window, textvariable=string_var)
entry1.pack()

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

# run
window.mainloop()


