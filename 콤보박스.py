import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("making GUI")
root.geometry("640x480+400+100")

values = [str(i) + "일" for i in range(1, 32)] # 1~31부터의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") #read only = 읽기전용임
readonly_combobox.current(0) # 0번째 인덱스 값 자동 설정
readonly_combobox.pack()    

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()