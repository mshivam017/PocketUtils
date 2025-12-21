import PIL
from PIL import Image
from tkinter import Tk 
from tkinter.filedialog import *

root = Tk()
root.title("Image Compressor")
# root.geometry('1280x720+150+80')
# root.configure(bg='#323846')
# root.resizable(False, False)

file_path = askopenfilename()
img=PIL.Image.open(file_path)
myHeight,myWidth=img.size

img = img.resize((myHeight,myWidth),PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+"compressed.jpg")
root.mainloop()
