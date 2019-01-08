#  (c) Adam Sawyer. 2018

from tkinter import *
from tkinter.messagebox import showinfo
import tracker_alarms
import tracker_calendar

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

        self.filemenu.add_command(label='Export Report', command=self.soonPopUp)
        self.filemenu.add_command(label='CALENDAR', command=self.showCalendar)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', command=self.quit)
        self.helpmenu.add_command(label='About', command=self.helpPopUp)
        root.config(menu=self.menus)

        for t in range(3):
            tracker_alarms.Timer(self.canvas, t+1, root)

    @staticmethod
    def soonPopUp():
        showinfo('Coming Soon', 'This feature will be implemented soon!')

    @staticmethod
    def showCalendar():
        tracker_calendar.UserCalendar.infoPop()


    @staticmethod
    def helpPopUp():
        showinfo('About', 'Source Code:\n'
                          'https://github.com/aesawyer/ProjectTimeTracker\n\n'
                          'Version\n'
                          '0.5')

    @staticmethod
    def quit():
        root.quit()
        sys.exit()

if __name__ == '__main__':
    root = Tk()
    app = UI()
    root.mainloop()
