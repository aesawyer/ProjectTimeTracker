#  (c) Adam Sawyer. 2018

from tkinter import ttk
from tkinter import *
import datetime
import os.path

class Timer:
    def __init__(self, canvas, count, root):
        self.canvas = canvas
        self.count = count
        self.timer = 0
        self.active = False
        self.widgets(self.canvas, self.count, root)

    def widgets(self, canvas, count, root):
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
        title = Entry(root, width=26, justify=CENTER)
        title.place(x=61+circnt, y=50, anchor=W)
        circle = canvas.create_oval(61+circnt, 90, (61+circnt)+166, 256, width=10, outline=fill)
        timerText = canvas.create_text(btncnt, 173, anchor=CENTER, fill='white', font=('Consolas', 18), text='0:00:00')
        startbtn = ttk.Button(text='Start', command=lambda: self.start(circle, fill, timerText, root))
        startbtnWin = canvas.create_window(btncnt-38, 300, anchor=CENTER, window=startbtn)
        pausebtn = ttk.Button(text='Pause', command=lambda: self.pause(timerText, root))
        pausebtnWin = canvas.create_window(btncnt+38, 300, anchor=CENTER, window=pausebtn)
        stopbtn = ttk.Button(text='Stop', command=lambda: self.stop(circle, fill, timerText, title, root))
        stopbtnWin = canvas.create_window(btncnt, 325, anchor=CENTER, window=stopbtn)

    def stopwatch(self, run, timerText, root):
        if self.active:
            self.canvas.itemconfig(timerText, fill='white')
            self.canvas.itemconfig(timerText, text=str(datetime.timedelta(seconds=self.timer)))
            self.timer += 1
            #print(str(datetime.timedelta(seconds=self.timer)))
            #print(self.timer)
            if run:
                root.after(1000, lambda: self.stopwatch(True, timerText, root))

    def circleChange(self, circle, fill):
        if self.canvas.itemcget(circle, 'fill') == '':
            self.canvas.itemconfig(circle, fill=fill)
        else:
            self.canvas.itemconfig(circle, fill='')

    def start(self, circle, fill, timerText, root):
        if not self.active:
            if self.canvas.itemcget(circle, 'fill') == '':
                self.circleChange(circle, fill)
            self.active = True
            self.stopwatch(True, timerText, root)

    def stop(self, circle, fill, timerText, title, root):
        if self.active:
            self.OutputLog(title, timerText)
            self.circleChange(circle, fill)
            self.active = False
            self.timer = 0
            self.stopwatch(False, timerText, root)

    def pause(self, timerText, root):
        if self.active:
            self.active = False
            self.canvas.itemconfig(timerText, fill='black')
            self.stopwatch(False, timerText, root)

    def OutputLog(self, title, timerText):
        #TODO Implement 'Browse Save Directory' Feature
        circTitle = title.get()
        timer = self.canvas.itemcget(timerText, 'text')
        now = str(datetime.datetime.now().date())
        if os.path.isfile('outputlog.txt'):
            f = open('outputlog.txt', 'a')
            content = '\n' + now + ' | ' + circTitle + ' | ' + timer
        else:
            f = open('outputlog.txt', 'w')
            content = now + ' | ' + circTitle + ' | ' + timer
        f.write(content)
        f.close()
        pass