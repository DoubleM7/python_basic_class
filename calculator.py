from tkinter import *

def button_pressed(value):
  if value == "AC":
    entry.delete(0, 'end')
  else: # 그 외(숫자 및 계산 버튼)
    entry.insert('end', value)

def equal_button_pressed():
  try:
    result = eval(entry.get())
  except:
    pass
  else:
    entry.delete(0, 'end')
    entry.insert('end', str(result))

tk = Tk()
tk.title("Calculator")
tk.geometry("300x200")

entry = Entry(tk, width = 20)
entry.grid(row=0, columnspan=3)


# 숫자 버튼
button1 = Button(tk, text = "1", command = lambda : button_pressed('1'))
button1.grid(row=1, column=0)

button2 = Button(tk, text = "2", command = lambda : button_pressed('2'))
button2.grid(row=1, column=1)

button3 = Button(tk, text = "3", command = lambda : button_pressed('3'))
button3.grid(row=1, column=2)

button4 = Button(tk, text = "4", command = lambda : button_pressed('4'))
button4.grid(row=2, column=0)

button5 = Button(tk, text = "5", command = lambda : button_pressed('5'))
button5.grid(row=2, column=1)

button6 = Button(tk, text = "6", command = lambda : button_pressed('6'))
button6.grid(row=2, column=2)

button7 = Button(tk, text = "7", command = lambda : button_pressed('7'))
button7.grid(row=3, column=0)

button8 = Button(tk, text = "8", command = lambda : button_pressed('8'))
button8.grid(row=3, column=1)

button9 = Button(tk, text = "9", command = lambda : button_pressed('9'))
button9.grid(row=3, column=2)

button0 = Button(tk, text = "0", command = lambda : button_pressed('0'))
button0.grid(row=4, column=1)

buttonAC = Button(tk, text = "AC", command = lambda : button_pressed('AC'))
buttonAC.grid(row=4, column=0)

buttonEqual = Button(tk, text = "=", command = equal_button_pressed)
buttonEqual.grid(row=4, column=2)

buttonDiv = Button(tk, text = "/", command = lambda : button_pressed('/'))
buttonDiv.grid(row=1, column=3)

buttonMul = Button(tk, text = "*", command = lambda : button_pressed('*'))
buttonMul.grid(row=2, column=3)

buttonPlus = Button(tk, text = "+", command = lambda : button_pressed('+'))
buttonPlus.grid(row=3, column=3)

buttonSub = Button(tk, text = "-", command = lambda : button_pressed('-'))
buttonSub.grid(row=4, column=3)



tk.mainloop()