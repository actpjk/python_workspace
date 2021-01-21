from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = 'right', fill = 'y')

# set이 없으면 scroll을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode = 'extended', height=10, yscrollcommand = scrollbar.set)

for i in range(1, 32): # 1 ~ 31일 정보
    listbox.insert(END, str(i) + '일')

scrollbar.config(command = listbox.yview) # scrollbar 에도 mapping , 서로를 mapping 해줘야함 listbox <-> scrollbar

listbox.pack(side = 'left')



root.mainloop()