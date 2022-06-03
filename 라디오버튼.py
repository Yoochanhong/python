from tkinter import *

root = Tk()
root.title("making GUI")
root.geometry("640x480+400+100")

Label(root, text = "메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burgel1 = Radiobutton(root, text="불고기버거", value=1, variable = burger_var)
btn_burgel1.select() #기본값으로 불고기버거
btn_burgel2 = Radiobutton(root, text="치즈버거", value=2, variable =burger_var)
btn_burgel3 = Radiobutton(root, text="새우버거", value=3, variable =burger_var)

btn_burgel1.pack()
btn_burgel2.pack()
btn_burgel3.pack()

Label(root, text = "음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable = drink_var)
btn_drink1.select() #기본값으로 콜라
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable = drink_var)
btn_drink3 = Radiobutton(root, text="초코에몽", value="초코에몽", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 선택된 햄버거 값(radio)을 출력
    print(drink_var.get()) # 선택된 음료수 값(radio)을 출력

btn = Button(root, text="주문하기", command=btncmd)
btn.pack()

root.mainloop()