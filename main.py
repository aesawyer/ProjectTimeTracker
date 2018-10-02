from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import time
import datetime

class Timer:
    def __init__(self, root, canvas, count):
        self.root = root
        self.canvas = canvas
        self.count = count
        self.timer = 0
        self.active = False
        self.widgets(self.canvas, self.count)

    def widgets(self, canvas, count):
        if count == 1:
            circnt = 0
            btncnt = 144  #middle-x of first circle
            fill = '#FF1D25'
        elif count == 2:
            circnt = 267  #difference in space between top-x of circles
            btncnt = 61+circnt+83  #61=top-x of circle, 83 is radius of circle
            fill = '#3FA9F5'
        elif count == 3:
            circnt = 534
            btncnt = 61+circnt+83
            fill = '#7AC943'
        title = Entry(self.root, width=26, justify=CENTER)
        title.place(x=61+circnt, y=50, anchor=W)
        circle = canvas.create_oval(61+circnt, 90, (61+circnt)+166, 256, width=10, outline=fill)
        timerText = canvas.create_text(btncnt, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
        startbtn = ttk.Button(text='Start', command=lambda: self.start(circle, fill))
        startbtnWin = canvas.create_window(btncnt-38, 300, anchor=CENTER, window=startbtn)
        pausebtn = ttk.Button(text='Pause', command=lambda: self.pause(circle, fill))
        pausebtnWin = canvas.create_window(btncnt+38, 300, anchor=CENTER, window=pausebtn)
        stopbtn = ttk.Button(text='Stop', command=lambda: self.stop(circle, fill))
        stopbtnWin = canvas.create_window(btncnt, 325, anchor=CENTER, window=stopbtn)

    def stopwatch(self, run):
        if self.active:
            self.timer += 1
            if run:
                root.after(1000, self.timer)

    def circleChange(self, circle, fill):
        if self.canvas.itemcget(circle, 'fill') == '':
            self.canvas.itemconfig(circle, fill=fill)
        else:
            self.canvas.itemconfig(circle, fill='')

    def start(self, circle, fill):
        if not self.active:
            self.circleChange(circle, fill)
            self.active = True
            self.stopwatch(True)

    def stop(self, circle, fill):
        if self.active:
            self.circleChange(circle, fill)
            self.active = False
            self.stopwatch(False)

    def pause(self, circle, fill):
        if self.active:
            pass
        pass

class UI:
    #Base Appearance-----------------------------------------------------
    def __init__(self):
        root.title("Project Time Tracker")
        root.resizable(width=False, height=False)
        root.geometry('800x400')
        self.canvas = Canvas(root, width=820, height=420, bg='gray25')
        self.canvas.place(x=-5, y=-5)
        self.canvas.create_rectangle(100, 350, 850, 450, outline='', fill='#ff6600')
        #self.canvas.create_rectangle(100, 100, 200, 200, outline='', fill='#fff000')
        self.canvas.create_oval(50, 350, 150, 500, outline='', fill='#ff6600')

        #File Menus-----------------------------------------------------
        self.menus = Menu(root)
        self.filemenu = Menu(self.menus, tearoff=0)
        self.helpmenu = Menu(self.menus, tearoff=0)

        self.menus.add_cascade(label='File', menu=self.filemenu)
        self.menus.add_cascade(label='Help', menu=self.helpmenu)

        self.filemenu.add_command(label='Export Report')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Reset')
        self.filemenu.add_command(label='Quit', command=self.quit)
        self.helpmenu.add_command(label='About', command=self.helpPopUp)
        root.config(menu=self.menus)

        for t in range(3):
            Timer(root, self.canvas, t+1)

    @staticmethod
    def helpPopUp():
        showinfo('About', 'Source Code:\n'
                          'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                          'Version\n'
                          '0.1')

    @staticmethod
    def quit():
        root.quit()
        sys.exit()

if __name__ == '__main__':
    root = Tk()
    app = UI()
    root.mainloop()
