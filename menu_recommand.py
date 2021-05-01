from tkinter import *
from PIL import Image, ImageTk

def change_image():
  global x
  global img_list
  global image_after
  label.config(image = img_list[x])
  x = x + 1
  x = x % 5
  image_after = tk.after(100, change_image)

def stop():
  global image_after
  tk.after_cancel(image_after)

tk = Tk()
tk.title("Menu")
x = 0
image_after = None

img1 = Image.open("images/food1.jpg")
img2 = Image.open("images/food2.jpg")
img3 = Image.open("images/food3.jpg")
img4 = Image.open("images/food4.jpg")
img5 = Image.open("images/food5.jpg")
img1 = img1.resize((300, 300), Image.ANTIALIAS)
img2 = img2.resize((300, 300), Image.ANTIALIAS)
img3 = img3.resize((300, 300), Image.ANTIALIAS)
img4 = img4.resize((300, 300), Image.ANTIALIAS)
img5 = img5.resize((300, 300), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
img2 = ImageTk.PhotoImage(img2)
img3 = ImageTk.PhotoImage(img3)
img4 = ImageTk.PhotoImage(img4)
img5 = ImageTk.PhotoImage(img5)
img_list = [img1, img2, img3, img4, img5]
label = Label()
label.pack()

button = Button(text = "Stop!", command = stop)
button.pack()
change_image()

tk.mainloop()