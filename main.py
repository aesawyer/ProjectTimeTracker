from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

def helpPopUp():
    showinfo('About', 'Source Code:\n'
                      'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                      'Version\n'
                      '0.1')

def initUI():
    c1 = canvas.create_oval(50, 75, 216, 241, width=10, outline='#FF1D25')  # 166 width/height difference
    c2 = canvas.create_oval(317, 75, 483, 241, width=10, outline='#3FA9F5')
    c3 = canvas.create_oval(584, 75, 750, 241, width=10, outline='#7AC943')

root = Tk()
root.title("Project Time Tracker")
root.geometry('800x400')
canvas = Canvas(root, width=800, height=400, bg='gray69')
canvas.pack()

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

timer1 = ttk.Button(text='Start', command=helpPopUp)
timer1Window = canvas.create_window(133, 300, anchor=CENTER, window=timer1)

timer2 = ttk.Button(text='Start', command=helpPopUp)
timer2Window = canvas.create_window(400, 300, anchor=CENTER, window=timer2)

timer3 = ttk.Button(text='Start', command=helpPopUp)
timer3Window = canvas.create_window(667, 300, anchor=CENTER, window=timer3)

initUI()
root.config(menu=menus)
root.mainloop()