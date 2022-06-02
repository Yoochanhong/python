from tkinter import *

root = Tk()
root.title("making GUI")#제목
root.geometry("640x480+400+100") #가로 * 세로 + X좌표 + Y좌표
#root.resizable(False, False) # x(너비), y(높이) 변경 불가 (창 크기 변경 불가)
btn1 = Button(root, text="버튼1")
btn1.pack()
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
photo = PhotoImage(file="제목 없음.png")
btn6 = Button(root, image=photo)
btn6.pack()
def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()
label1 = Label(root, text="안녕하세요")
label1.pack()
photo = PhotoImage(file="제목 없음.png")
label2 = Label(root, image=photo)
label2.pack()
def change():
    label1.config(text="버튼 누름")
    global photo2#전역변수

    photo2 = PhotoImage(file="제목 없음22.png")
    label2.config(image=photo2)
btn8 = Button(root, text="클릭", command=change)
btn8.pack()
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")
e = Entry(root, width=30)
e.pack()
root.mainloop()