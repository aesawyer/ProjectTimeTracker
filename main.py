from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import time
import datetime

def helpPopUp():
    showinfo('About', 'Source Code:\n'
                      'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                      'Version\n'
                      '0.1')

def timerControl(timer, active, timerText):
    if timer > 0:
        timer = 0
    print('step 1')
    while active:
        time.sleep(1)
        timer += 1
        print('step' + str(timer))
        #canvas.itemconfig(timerText, text=str(datetime.timedelta(seconds=timer)))

def circleChange(circle, fill, timer, active, timerText):
    if canvas.itemcget(circle, 'fill') == '' and not active:
        canvas.itemconfig(circle, fill=fill)
        active = True
        timerControl(timer, active, timerText)
    else:
        canvas.itemconfig(circle, fill='')
        active = False
        timerControl(timer, active, timerText)

#Base Appearance
root = Tk()
root.title("Project Time Tracker")
root.resizable(width=False, height=False)
root.geometry('800x400')
canvas = Canvas(root, width=800, height=400, bg='gray25')
canvas.pack()
canvas.create_rectangle(100, 350, 850, 450, outline='', fill='#ff6600')
canvas.create_oval(50, 350, 150, 500, outline='', fill='#ff6600')

#File Menus
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

#Timers
timer1 = ttk.Button(text='Start', command=lambda: circleChange(c1, '#FF1D25', c1timer, c1timerActive, c1TimerText))
timer1Window = canvas.create_window(133, 300, anchor=CENTER, window=timer1)
c1 = canvas.create_oval(50, 90, 216, 256, width=10, outline='#FF1D25', fill='')
c1timer = 0
c1timerActive = False
c1TimerText = canvas.create_text(133, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c1Title = Entry(root, justify=CENTER)
c1Title.place(x=133, y=50, anchor=CENTER)

timer2 = ttk.Button(text='Start', command=lambda: circleChange(c2, '#3FA9F5', c2timer, c2timerActive, c2TimerText))
timer2Window = canvas.create_window(400, 300, anchor=CENTER, window=timer2)
c2 = canvas.create_oval(317, 90, 483, 256, width=10, outline='#3FA9F5')
c2timer = 0
c2timerActive = False
c2TimerText = canvas.create_text(400, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c2Title = Entry(root, justify=CENTER)
c2Title.place(x=400, y=50, anchor=CENTER)

timer3 = ttk.Button(text='Start', command=lambda: circleChange(c3, '#7AC943', c3timer, c3timerActive, c3TimerText))
timer3Window = canvas.create_window(667, 300, anchor=CENTER, window=timer3)
c3 = canvas.create_oval(584, 90, 750, 256, width=10, outline='#7AC943')
c3timer = 0
c3timerActive = False
c3TimerText = canvas.create_text(667, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c3Title = Entry(root, justify=CENTER)
c3Title.place(x=667, y=50, anchor=CENTER)

root.config(menu=menus)
root.mainloop()
