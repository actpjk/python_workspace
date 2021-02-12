from tkinter import *

root = Tk()
root.title('제목 없음 - windows 메모장')
root.geometry('640x480')

txt = Text(root)
txt.pack(side='left', fill= 'both', expand=True)

scrollbar = Scrollbar(txt)
scrollbar.pack(side= 'right', fill ='y')


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label = '열기')
menu_file.add_command(label = '저장')
menu_file.add_command(label = '끝내기', command = root.quit)
menu.add_cascade(label = '파일', menu = menu_file)
menu.add_cascade(label = '편집')
menu.add_cascade(label = '서식')
menu.add_cascade(label = '보기')
menu.add_cascade(label = '도움말')



root.config(menu=menu)

root.mainloop()