'''
There are 2 major ways to get data from widgets

1. Tkinter variables  --- most used

2. get()  --- lots of widgets have obvious data that user want to get. for this --> get()
   ex: entry has get() that returns its text

****
Note: All widgets dont have get() method.  ex: label doesnt have get method
where as entry widget has get() ---> entry.get()  --- fetches the text typed in the entry widget
****

widgets can be updated with configure() method
ex: Label.configure(text='some new text')   
equivalent: Label['text'] = 'some new text'

*****
Note: To know different that you can perform on certain widget ----> use configure() method without any arguments
ex: print(label.configure())
*****

'''

import tkinter as tk 
from tkinter import ttk

def button_func():
  
  # get the content of the entry
  # print(entry.get())
  entry_text = entry.get()   # dynamic text
  
  # update the label
  # label.configure(text = 'some other text') 
  label['text'] = entry_text

  # disable entry widget after button is pressed
  entry['state'] = 'disabled'

  # to print different operations that can be performed on etnry widget ---> entry.configure()
  print(entry.configure())
  

# window

window = tk.Tk()
window.title('get and set widget')
window.geometry('500x300')

# widgets

label = ttk.Label(master = window, text = 'This is label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The Button', command = button_func)
button.pack()

# run

window.mainloop()



