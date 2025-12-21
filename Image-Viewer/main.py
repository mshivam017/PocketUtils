from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def showImage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image file', filetypes=(('JPG File', '*.jpg'),('PNG File','*.png'),('All File','how are you .txt')))
    img = Image.open(filename)
    img= ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img

root= Tk()
frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn= Button(frame,text='Select Image',command=showImage)
btn.pack(side=tk.LEFT)

btn2= Button(frame,text='Exit',command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.title('Image Viewer')
root.geometry('400x450')
root.mainloop()