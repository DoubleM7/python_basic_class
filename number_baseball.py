from tkinter import *
import tkinter.messagebox as msgbox
import random


def random_num():
  nums = random.sample(range(1, 10), 4)
  return nums

def check_answer(nums, entry):
  global score
  entry_num = []
  strike = 0
  if check_condition():
    for i in range(4):
      entry_num.append(int(entry[i].get()))
    same_num = len(set(entry_num) & set(nums))
    for i in range(4):
      if entry_num[i] == nums[i]:
        strike += 1
    ball = same_num - strike
    listbox.insert(END, f"{entry_num[0]}, {entry_num[1]}, {entry_num[2]}, {entry_num[3]}: {ball} Ball, {strike} Strike")
  
  if strike == 4:
    msgbox.showinfo(title = "Congratulation!", 
    message = f"Your score is {score}")
    tk.quit()
  else:
    score -= 1
  if score == 0:
    msgbox.showinfo(title = "Oh no!", message = "Game Over!")
    tk.quit()
    

def check_condition():
  entry_num = []
  for i in range(4):
    if int(entry[i].get()) < 1 or int(entry[i].get()) > 9:
      msgbox.showinfo(title = "Try Again!", 
      message = "Check Range!")
      return False
    else:
      entry_num.append(int(entry[i].get()))
  if len(set(entry_num)) != 4:
    msgbox.showinfo(title = "Try Again!", 
    message = "Put 4 different numbers!")
    return False
  return True


nums = random_num()
score = 10
tk = Tk()
tk.title("Number Baseball Game")
tk.geometry("210x250")

entry = []

for i in range(4):
  entry.append(Entry(tk, width = 5))
  entry[i].grid(row = 0, column = i)
button = Button(text = "Check!")
button.config(command = lambda: check_answer(nums, entry))
button.grid(row = 1, columnspan = 4)
listbox = Listbox(width = 25, height = 10)
listbox.grid(row=2, columnspan= 4)
tk.mainloop()