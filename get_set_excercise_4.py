'''
excercise - Add another button that changes text back to 'some text' and that enables entry

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
  # print(entry.configure())    # ************* IMPORTANT *************
  

# window

window = tk.Tk()
window.title('get and set widget')
window.geometry('500x300')

# widgets

label = ttk.Label(master = window, text = 'This is label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack(pady=5)

button = ttk.Button(master = window, text = 'The Button', command = button_func)
button.pack(pady=5)

# excercise

def reset_func():
  # change the text back to 'some other text'
  label['text'] = 'some other text'
  # enable the entry button
  entry['state'] = 'enabled'

excercise_button = ttk.Button(master=window, text='Excercise Button', command = reset_func )
excercise_button.pack(pady=5)


# run

window.mainloop()



