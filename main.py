from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import time
import datetime

'''
def circleChange(circle, fill):
    if canvas.itemcget(circle, 'fill') == '':
        canvas.itemconfig(circle, fill=fill)
    else:
        canvas.itemconfig(circle, fill='')
'''

class Timer:
    def __init__(self, root, canvas, count):
        self.root = root
        self.canvas = canvas
        self.count = count
        #self.x
        #self.y
        self.timer = 0
        self.active = False
        self.widgets(root, canvas, count)

    def widgets(self, root, canvas, count):
        if count == 1:
            circnt = 0
            btncnt = 144 #middle of first circle
            fill = '#FF1D25'
        elif count == 2:
            circnt = 267 #difference in space between top-x of circles
            btncnt = 61+circnt+83 #61=top-x of circle, 83 is radius of circle
            fill = '#3FA9F5'
        elif count == 3:
            circnt = 534
            btncnt = 61+circnt+83
            fill = '#7AC943'
        title = Entry(root, width=26, justify=CENTER)
        title.place(x=61+circnt, y=50, anchor=W)
        clbtn_txt = StringVar()
        #clbtn = ttk.Button(textvariable=clbtn_txt, command=self.stateChange)
        clbtn = ttk.Button(text='Start', command=self.stateChange)
        clbtn_txt.set('Start')
        timerWindow = canvas.create_window(btncnt, 300, anchor=CENTER, window=clbtn)
        circle = canvas.create_oval(61+circnt, 90, (61+circnt)+166, 256, width=10, outline=fill)
        timerText = canvas.create_text(btncnt, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')

    def stateChange(self):
        if self.clbtn_txt.get() == 'Stop':
            self.clbtn_txt.set('Start')
            self.active = False
            #self.timerStart()
            #self.circleChange()
        else:
            self.clbtn_txt.set('Stop')
            self.timer = 0
            self.active = True
            # timerStart(timer, timerText, active)
            #self.circleChange()

class UI:
    #Base Appearance-----------------------------------------------------
    def __init__(self):
        self.root = Tk()
        self.root.title("Project Time Tracker")
        self.root.resizable(width=False, height=False)
        self.root.geometry('800x400')
        self.canvas = Canvas(self.root, width=820, height=420, bg='gray25')
        self.canvas.place(x=-5, y=-5)
        self.canvas.create_rectangle(100, 350, 850, 450, outline='', fill='#ff6600')
        #self.canvas.create_rectangle(100, 100, 200, 200, outline='', fill='#fff000')
        self.canvas.create_oval(50, 350, 150, 500, outline='', fill='#ff6600')

        #File Menus-----------------------------------------------------
        self.menus = Menu(self.root)
        self.filemenu = Menu(self.menus, tearoff=0)
        self.helpmenu = Menu(self.menus, tearoff=0)

        self.menus.add_cascade(label='File', menu=self.filemenu)
        self.menus.add_cascade(label='Help', menu=self.helpmenu)

        self.filemenu.add_command(label='Export Report')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Reset')
        self.filemenu.add_command(label='Quit', command=self.quit)
        self.helpmenu.add_command(label='About', command=self.helpPopUp)
        self.root.config(menu=self.menus)

        for t in range(3):
            Timer(self.root, self.canvas, t+1)

    @staticmethod
    def helpPopUp():
        showinfo('About', 'Source Code:\n'
                          'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                          'Version\n'
                          '0.1')

    @staticmethod
    def quit():
        app.root.quit()
        sys.exit()

if __name__ == '__main__':
    app = UI()
    app.root.mainloop()
