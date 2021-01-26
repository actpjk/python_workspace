from tkinter import *

root = Tk()
root.title('Samsung')
root.geometry('640x480')

listbox = Listbox(root, selectmode = 'extended', height=0)
listbox.insert(0, '미국 10년물 채권 금리')
listbox.insert(1, '제조업 선행 지수')
listbox.insert(2, '달러 지수')
listbox.insert(3, '원/달러 환율')
listbox.insert(END, '부동산 가격기대 지수')
listbox.insert(END, '인플레이션율')
listbox.pack()

def btncmd():
    listbox.delete(0) # 0 : 맨 앞 항목을 삭제, END : 맨 뒤 항목을 삭제

    # 갯수 확인
    # print('리스트에는', listbox.size(), '개가 있습니다.')

    # 항목 확인 (시작 idx, 끝 idx)
    # print('1번째부터 3번째까지의 항목 : ', listbox.get(0 ,2))

    # 선택된 항목 확인 (위치로 반환 ex : (1, 2, 3))
    print('선택된 항목 : ', listbox.curselection())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()