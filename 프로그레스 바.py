import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("making GUI")
root.geometry("640x480+400+100")

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #튕겨서 돌아옴
#progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #그대로 쭉 늘어남
#progressbar.start(10) #10ms마다 움직임
#progressbar.pack()
#
#def btncmd():
#    progressbar.stop() # 작동 중지
#
#btn = Button(root, text="중지", command=btncmd)
#btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): #1~100까지
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #progressbar2의 값 설정
        progressbar2.update() #ui업뎃
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()
root.mainloop()