import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')

values = [str(i) + '일' for i in range(1, 32) ] # 1~32 숫자 반환
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일')

readonly_combobox = ttk.Combobox(root, height=5, values=values, state = 'readonly')
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 출력
    print(readonly_combobox.get())


btn = Button(root, text='select', command=btncmd)
btn.pack()

root.mainloop()