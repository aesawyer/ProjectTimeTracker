from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import time

def helpPopUp():
    showinfo('Contact', 'Source Code: \n')

root = Tk()

root.title("Time-Productivity Tracker v.0")
menus = Menu(root)
filemenu = Menu(menus, tearoff=0)
helpmenu = Menu(menus, tearoff=0)

menus.add_cascade(label='File', menu=filemenu)
menus.add_cascade(label='Help', menu=helpmenu)

filemenu.add_command(label='Export Report')
filemenu.add_separator()
filemenu.add_command(label='Reset')
filemenu.add_command(label='Quit', command=root.quit)
helpmenu.add_command(label='Contact', command=helpPopUp)

timer = ttk.Button(text='Track').grid()
root.config(menu=menus)
root.mainloop()