import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate')
# progressbar = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()


# btn1 = Button(root, text = '중지', command=btncmd)
# btn1.pack()

p_var2 = DoubleVar() # 실수(float)도 반영하기 위해서
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 초 대기
        
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn2 = Button(root, text = '시작', command=btncmd2)
btn2.pack()

root.mainloop()