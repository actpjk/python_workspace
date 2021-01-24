from tkinter import *
from tkinter import messagebox as msgbox 
import tkinter.ttk as ttk
from tkinter import filedialog

root = Tk()
root.title('Data_Loader')
root.geometry('700x500')

# filename = str(combobox.get())
# def saving():
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(txt.get('1.0', END))
#         pass # 모든 내용을 가져와서 저장


# 파일 프레임 (선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = 'x', padx=5, pady=5) # 간격 띄우기

def cmb_select():
    pass


kospi = 
a10rate = 
dollaridx = 
gold = 
slv = 

values = [str(kospi.get()), a10rate.get(), dollaridx.get(), gold.get(), slv.get()]
combobox = ttk.Combobox(file_frame, height=3, width=60, values=values, state = 'readonly')
combobox.pack(side = 'left', fill='both',padx=5, pady=5)
combobox.set('Data list')

btn_del_file = Button(file_frame, padx=5, pady=5, width=20, text='선택 삭제')
btn_del_file.pack(side = 'right',padx=20, pady=5)

# btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text = '파일 추가')
# btn_add_file.pack(side = 'right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill = 'both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = 'right', fill='y')

list_file = Listbox(list_frame, selectmode = 'extended', height=10, yscrollcommand = scrollbar.set)
list_file.pack(side = 'left', fill = 'both', expand=True)
scrollbar.config(command = list_file.yview)

# 옵션 프레임
frame_option = LabelFrame(root, text = '옵션')
frame_option.pack(fill = 'x', padx=5, pady=5, ipady=5)

# 저장경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill = 'x',padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side = 'left', fill = 'x', expand=True, padx=5, pady=5, ipady=4) #ipady : 높이 변경

btn_dest_path = Button(path_frame, text = '찾아보기', width = 10)
btn_dest_path.pack(side = 'right',padx=5, pady=5)


# 1. 파일 형식 옵션
    # 파일 형식 옵션 레이블
lbl_format = Label(frame_option, text = '파일 형식', width = 8)
lbl_format.pack(side = 'left', padx=5, pady=5)
    
    # 파일 형식 옵션 콤보
opt_format = ['csv', 'xls']
cmb_format = ttk.Combobox(frame_option, state = 'readonly', values = opt_format, width = 10)
cmb_format.current(0)
cmb_format.pack(side = 'left', padx=5, pady=5)

# 2. 기간 선택 옵션
    # 기간 선택 레이블
lbl_width = Label(frame_option, text = '기간 선택', width = 8)
lbl_width.pack(side = 'left', padx=5, pady=5)

    # 기간 선택 콤보박스
opt_width = ['일간', '월간', '연간']
cmb_width = ttk.Combobox(frame_option, state = 'readonly', values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side = 'left', padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text = '진행상황')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill ='x', padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text='닫기', width='12', command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)

btn_start = Button(frame_run, padx =5, pady=5, text='시작', width='12')
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False, False)
root.mainloop()