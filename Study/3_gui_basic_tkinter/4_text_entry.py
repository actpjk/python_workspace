from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, '글자를 입력하세요.')

e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력해요.')

def btncmd():
    # 내용 출력
    print(txt.get('1.0', END)) # 처음부터 끝까지 모든 txt 내용 가져옴, 1 : 첫번째 라인, 0 : 0번째 컬럼 위치 라인 1부터 0은 컬럼 기준 0번째 위치부터 가져옴(1.0)
    print(e.get())

    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()