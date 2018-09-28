from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import threading
import time
import datetime

def helpPopUp():
    showinfo('About', 'Source Code:\n'
                      'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                      'Version\n'
                      '0.1')

def stateChange(circle, timer, fill, timerText, button, active):
    if button.get() == 'Stop':
        button.set('Start')
        active = False
        timerStart(timer, timerText, active)
        circleChange(circle, fill)
        return
    else:
        button.set('Stop')
        active = True
        timer = 0
        thread = threading.Thread(target=timerStart, args=(timer, timerText, active))
        thread.daemon = True
        thread.start()
        circleChange(circle, fill)
        return

def timerStart(timer, timerText, active):
    while active:
        time.sleep(1)
        timer += 1
        print(timer)

def timerStop(timer, timerText):
    print('timerStop')

def circleChange(circle, fill):
    if canvas.itemcget(circle, 'fill') == '':
        canvas.itemconfig(circle, fill=fill)
    else:
        canvas.itemconfig(circle, fill='')

#Base Appearance-----------------------------------------------------
root = Tk()
root.title("Project Time Tracker")
root.resizable(width=False, height=False)
root.geometry('800x400')
canvas = Canvas(root, width=800, height=400, bg='gray25')
canvas.pack()
canvas.create_rectangle(100, 350, 850, 450, outline='', fill='#ff6600')
canvas.create_oval(50, 350, 150, 500, outline='', fill='#ff6600')

#File Menus-----------------------------------------------------
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

#Timers-----------------------------------------------------
c1timer = 0
c1Active = False
c1btn_txt = StringVar()
c1btn = ttk.Button(textvariable=c1btn_txt, command=lambda: stateChange(c1, c1timer, '#FF1D25', c1TimerText, c1btn_txt, c1Active))
c1btn_txt.set('Start')
timer1Window = canvas.create_window(133, 300, anchor=CENTER, window=c1btn)
c1 = canvas.create_oval(50, 90, 216, 256, width=10, outline='#FF1D25', fill='')
c1TimerText = canvas.create_text(133, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c1Title = Entry(root, justify=CENTER)
c1Title.place(x=133, y=50, anchor=CENTER)

c2timer = 0
c2Active = False
c2btn_txt = StringVar()
c2btn = ttk.Button(textvariable=c2btn_txt, command=lambda: stateChange(c2, c2timer, '#3FA9F5', c2TimerText, c2btn_txt, c2Active))
c2btn_txt.set('Start')
timer2Window = canvas.create_window(400, 300, anchor=CENTER, window=c2btn)
c2 = canvas.create_oval(317, 90, 483, 256, width=10, outline='#3FA9F5')
c2TimerText = canvas.create_text(400, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c2Title = Entry(root, justify=CENTER)
c2Title.place(x=400, y=50, anchor=CENTER)

c3timer = 0
c3Active = False
c3btn_txt = StringVar()
c3btn = ttk.Button(textvariable=c3btn_txt, command=lambda: stateChange(c3, c3timer, '#7AC943', c3TimerText, c3btn_txt, c3Active))
c3btn_txt.set('Start')
timer3Window = canvas.create_window(667, 300, anchor=CENTER, window=c3btn)
c3 = canvas.create_oval(584, 90, 750, 256, width=10, outline='#7AC943')
c3TimerText = canvas.create_text(667, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
c3Title = Entry(root, justify=CENTER)
c3Title.place(x=667, y=50, anchor=CENTER)


#thread = threading.Thread(target=timerStart, args=(timer, timerText))
#thread.daemon = True
#thread.start()
root.config(menu=menus)
root.mainloop()
