import keyboard
import time
from PIL import ImageGrab
from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import filedialog
import os

root = Tk()
root.title('@Auto screenshot@')
root.geometry('300x165')

# 시작 및 종료 키 설정

e = Entry(root, width=4)
e.pack(fill = 'both')
e.insert(0, 'F9')

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20210109_102030
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    # img.save('image{}.png'.format(curr_time)) # ex) image_20210109_102030.png
    dest_path = os.path.join(txt_dest_path.get(), 'image{}.png'.format(curr_time)) # 실제로 이미지가 저장되는 경로
    img.save(dest_path)

def start():
    setting_key = e.get()
    keyboard.add_hotkey(setting_key, screenshot)
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning('경고', '저장 경로를 선택하세요.')
        return 

# 저장 경로(폴더)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 누를 때
        print('폴더 선택 취소')
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 저장경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill = 'x',padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame) # delete 시 , text 였다면 ('1.0', END)
txt_dest_path.pack(side = 'left', fill = 'x', expand=True, padx=5, pady=5, ipady=4) #ipady : 높이 변경

btn_dest_path = Button(path_frame, text = '찾아보기', width = 10, command = browse_dest_path)
btn_dest_path.pack(side = 'right',padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_exit = Button(frame_run, padx =5, pady=5, text='종료', width='12', command = root.quit)
btn_exit.pack(side='right', padx=5, pady=5)

# btn_stop = Button(frame_run, padx =5, pady=5, text='중지', width='12', command = stop)
# btn_stop.pack(side='right', padx=5, pady=5)

btn_start = Button(frame_run, padx =5, pady=5, text='시작', width='12', command = start)
btn_start.pack(side='right', padx=5, pady=5)

label = Label(root, text = 'HelloCloud')
label.pack(side = 'right', fill='x')



root.resizable(False, False)

root.mainloop()