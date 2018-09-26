from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

import time

def helpPopUp():
    showinfo('About', 'Source Code:\n'
                        'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                        'Version\n'
                        '0.1')

root = Tk()
root.title("Project Time Tracker")
canvas = Canvas(root, width=800, height=400)
root.geometry('800x400')
menus = Menu(root)
filemenu = Menu(menus, tearoff=0)
helpmenu = Menu(menus, tearoff=0)

menus.add_cascade(label='File', menu=filemenu)
menus.add_cascade(label='Help', menu=helpmenu)

filemenu.add_command(label='Export Report')
filemenu.add_separator()
filemenu.add_command(label='Reset')
filemenu.add_command(label='Quit', command=root.quit)
helpmenu.add_command(label='About', command=helpPopUp)

c1 = PhotoImage(file='img/c1out.pgm')
canvas.create_image(200,200, anchor=NW, image=c1)
timer = ttk.Button(text='start').grid()

root.config(menu=menus)
root.mainloop()