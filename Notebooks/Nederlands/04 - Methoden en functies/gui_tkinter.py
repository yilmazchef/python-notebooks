# gui.py

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# add a textbox and a button

txt =  ttk.Entry(frm, width=20)

txt.grid(column=0, row=0)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()