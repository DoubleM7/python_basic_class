from tkinter import *
import random
import time

lotto = random.sample(range(1, 46), 6)

def check_condition():
  num = []
  for i in range(6):
    try:
      lot_num = int(lotto_entry[i].get())
    except ValueError:
      print("문자 말고 숫자를 입력하세요.")
      return

    if lot_num > 45 or lot_num < 1:
      print("1~45번 사이 숫자를 골라주세요.")
      return
    elif lot_num in num:
      print("중복되지 않게 골라주세요.")
      return
    else:
      num.append(lot_num)
  print_result()

def print_result():
  global lotto
  print("로또 번호를 공개합니다.")
  for i in lotto:
    print(i)
    time.sleep(1)
  check_lotto(lotto)

def check_lotto(lotto):
  num = []
  for i in range(6):
    num.append(int(lotto_entry[i].get()))
  score = len(set(lotto) & set(num))
  if score == 6:
    print("축하합니다. 1등입니다.")
  elif score == 5:
    print("축하합니다. 2등입니다.")
  elif score == 4:
    print("축하합니다. 3등입니다.")
  else:
    print("아쉽지만 다음 기회에...")


tk = Tk()
lotto_entry = []

for i in range(6):
  lotto_entry.append(Entry(tk, width = 10))
  lotto_entry[i].pack()

btn = Button(text = "Check lotto", command = check_condition)
btn.pack()

tk.mainloop()