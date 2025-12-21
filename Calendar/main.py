from tkinter import *
from tkcalendar import *
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
mycal =  Calendar(root,setmode='day',date_pattern='d/m/yy')
mycal.pack(padx=15,pady=35)

    # root.geometry('300x300')
root.title('Calendar')
root.configure(bg='lightblue')
icon_path = resource_path('calendar.ico')
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
root.mainloop()
