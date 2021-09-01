from tkinter import *
from tkinter.ttk import *

from time import strftime
import datetime as dt
root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root,font=("ds-digital",80), background="black",foreground="cyan",pad=0.3)
label.pack(anchor='center')
time()

mainloop()