from tkinter import *

root = Tk()
root.title("making GUI")
root.geometry("640x480+400+100")

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() #자동 선택처리
#chkbox.deselect() # 선택 해제처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="그냥 안보기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0일때는 체크 해제, 1일때는 체크 
    print(chkvar2.get()) # 얘도 똑같음

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()