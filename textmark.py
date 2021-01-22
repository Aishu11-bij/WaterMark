from PIL import Image, ImageDraw,ImageFont
import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
root = Tk()

root.filename = filedialog.askopenfilename(initialdir="/", title="Select A file",
                                           filetypes=(("png files", ".png"),
                                                      ("jpg files", "jpg"),
                                                      ("all files", ".")))
my_label = Label(root, text=root.filename).pack()
upload_img = ImageTk.PhotoImage(Image.open(root.filename))
upload_img_label = Label(image=upload_img).pack()

root.mainloop()

image = Image.open(root.filename)
font1 = ImageFont.truetype("arial.ttf",20)
draw = ImageDraw.Draw(image)
points1 = 000,000
points2 = 00,30
print("enter the name and age of person")
name = input()

print("enter the age of person")
age = input()

draw.text(points1,name,"white",font=font1)

draw.text(points2,age,"white",font=font1)
image.show()

