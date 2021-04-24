from tkinter import *
from PIL import Image, ImageTk

menu = ["Choco Latte", "Strawberry Latte", "Milk Tea", "Americano"]
price = [5000, 6000, 4000, 2500]

order_num = 0

def order():
  global order_num
  if entry_price.get() == "0":
    print("메뉴를 선택하세요.")
    return
  order_num += 1
  print("="*50)
  print("주문 번호 : ", order_num)
  print("="*50)
  print("주문 메뉴")
  print("-"*50)
  order_list = order_listbox.get(first=0, last=END)
  for i in order_list:
    print(i)
  print("총 금액 : ", entry_price.get(), "원 입니다.")
  print("-"*50)
  order_listbox.delete(0, END)
  entry_price.delete(0, END)
  entry_price.insert(0, "0")

def select_menu(value):
  order_listbox.insert(END, menu[value])
  cal_price(0, value)

def cal_price(op, value):
  tmp_price = int(entry_price.get())
  if op == 0:
    tmp_price += price[value]
  elif op == 1:
    tmp_price -= price[value]
  entry_price.delete(0, END)
  entry_price.insert(0, str(tmp_price))


def cancel_menu():
  try:
    delete_index = order_listbox.curselection()
    menu_index = menu.index(order_listbox.get(delete_index))
  except Exception:
    print("취소할 메뉴를 선택하세요.")
  else:
    order_listbox.delete(delete_index)
    cal_price(1, menu_index)

tk = Tk()
tk.title("Kiosk")
tk.geometry("500x400")

image_menu1 = Image.open("images/menu1.png")
image_menu1 = image_menu1.resize((100, 100), Image.ANTIALIAS)
image_menu1 = ImageTk.PhotoImage(image_menu1)

button_menu1 = Button(tk, image = image_menu1, command = 
lambda : select_menu(0))
button_menu1.grid(row=0, column=0)

image_menu2 = Image.open("images/menu2.png")
image_menu2 = image_menu2.resize((100, 100), Image.ANTIALIAS)
image_menu2 = ImageTk.PhotoImage(image_menu2)

button_menu2 = Button(tk, image = image_menu2, command = 
lambda : select_menu(1))
button_menu2.grid(row=0, column=1)

image_menu3 = Image.open("images/menu3.png")
image_menu3 = image_menu3.resize((100, 100), Image.ANTIALIAS)
image_menu3 = ImageTk.PhotoImage(image_menu3)

button_menu3 = Button(tk, image = image_menu3, command = 
lambda : select_menu(2))
button_menu3.grid(row=0, column=2)

image_menu4 = Image.open("images/menu4.png")
image_menu4 = image_menu4.resize((100, 100), Image.ANTIALIAS)
image_menu4 = ImageTk.PhotoImage(image_menu4)

button_menu4 = Button(tk, image = image_menu4, command = 
lambda : select_menu(3))
button_menu4.grid(row=0, column=3)

label_menu1 = Label(text = price[0])
label_menu1.grid(row = 1, column = 0)

label_menu2 = Label(text = price[1])
label_menu2.grid(row = 1, column = 1)

label_menu3 = Label(text = price[2])
label_menu3.grid(row = 1, column = 2)

label_menu4 = Label(text = price[3])
label_menu4.grid(row = 1, column = 3)

scroll = Scrollbar(orient = VERTICAL)
scroll.grid(row=2, column=4, sticky = N+S)

order_listbox = Listbox(width = 50, height = 5, yscrollcommand = scroll.set)
scroll['command'] = order_listbox.yview

order_listbox.grid(row=2, columnspan=4)

entry_price = Entry(width = 50)
entry_price.insert(0, "0")
entry_price.grid(row=3, columnspan=4)

button_cancel = Button(text = "Cancel", command = cancel_menu)
button_cancel.grid(row=4, column=0)

button_order = Button(text = "Order", command = order)
button_order.grid(row=4, column=1)


tk.mainloop()