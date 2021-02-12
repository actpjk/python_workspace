from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')

def creat_new_file():
    print('새 파일 만듭니다.')

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0) # tearoff	: 하위메뉴의 분리 기능 사용 유/무, 기본값 : False, 속성: Boolean
menu_file.add_command(label='New File', command=creat_new_file)
menu_file.add_command(label='New Window')
menu_file.add_separator()
menu_file.add_command(label='Opne File...')
menu_file.add_separator()
menu_file.add_command(label='Save All', state = 'disable') # 비활성화
menu_file.add_command(label = 'Exit', command=root.quit)

menu.add_cascade(label='File', menu=menu_file) # add_cascade : 상위 메뉴와 하위 메뉴 연결, 메뉴 이름.add_cascade(label="상위 메뉴 이름", menu=연결할 상위 메뉴)를 이용하여 메뉴를 부착할 수 있습니다.

# Edit 메뉴 (빈 값)
menu.add_cascade(label = 'Edit')

# Language 메뉴 추가 (radio 버튼 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='python')
menu_lang.add_radiobutton(label='java')
menu_lang.add_radiobutton(label='c++')
menu.add_cascade(label = 'Language', menu = menu_lang)


# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label = 'show minimap')
menu.add_cascade(label = 'view', menu = menu_view)

root.config(menu = menu)


root.mainloop()