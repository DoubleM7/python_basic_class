from tkinter import *
import tkinter.messagebox as msgbox

def check_winner():
  if ((b1["text"] == b2["text"] == b3["text"] == "O") or (b4["text"] == b5["text"] == b6["text"] == "O") or (b7["text"] == b8["text"] == b9["text"] == "O") or (b1["text"] == b4["text"] == b7["text"] == "O") or (b2["text"] == b5["text"] == b8["text"] == "O") or (b3["text"] == b6["text"] == b9["text"] == "O") or (b1["text"] == b5["text"] == b9["text"] == "O") or (b3["text"] == b5["text"] == b7["text"] == "O")):
    msgbox.showinfo(title = "Congratulation!", message = "Winner is Player1")
    tk.quit()

  elif ((b1["text"] == b2["text"] == b3["text"] == "X") or (b4["text"] == b5["text"] == b6["text"] == "X") or (b7["text"] == b8["text"] == b9["text"] == "X") or (b1["text"] == b4["text"] == b7["text"] == "X") or (b2["text"] == b5["text"] == b8["text"] == "X") or (b3["text"] == b6["text"] == b9["text"] == "X") or (b1["text"] == b5["text"] == b9["text"] == "X") or (b3["text"] == b5["text"] == b7["text"] == "X")):
    msgbox.showinfo(title = "Congratulation!", message = "Winner is Player2")
    tk.quit()
  else:
    if count == 9:
      msgbox.showinfo(title = "Oh no..", message = "No Winner..")
      tk.quit()


def change_color(button):
  global count
  if button["text"] == "":
    count += 1
  if count % 2 != 0: 
    button["text"] = "O"
    button["bg"] = "skyblue"
    button["activebackground"] = "skyblue"
  else:
    button["text"] = "X"
    button["bg"] = "yellow"
    button["activebackground"] = "yellow"
  if count >= 5:
    check_winner()

tk = Tk()
tk.title("Tic Tac Toe")

count = 0

label1 = Label(text = "Player 1 : O")
label2 = Label(text = "Player 2 : X")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

b1 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b1))
b2 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b2))
b3 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b3))
b4 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b4))
b5 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b5))
b6 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b6))
b7 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b7))
b8 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b8))
b9 = Button(text = "", height = 4, width = 8, bg = "white", activebackground="grey", command = lambda:change_color(b9))

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=4, column=0)
b8.grid(row=4, column=1)
b9.grid(row=4, column=2)

tk.mainloop()