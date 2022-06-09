from tkinter import *

root = Tk()
root.title("making GUI")
root.geometry("640x480+400+100")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# #btn1.pack(side="left") #왼쪽 끝
# #btn2.pack(side="right") #오른쪽 끝

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

#맨 윗줄
btn_f1 = Button(root, text="F1", width=5, height=2) # 크기를 x y 다 10씩 올려줌
btn_f2 = Button(root, text="F2", width=5, height=2)
btn_f3 = Button(root, text="F3", width=5, height=2)
btn_f4 = Button(root, text="F4", width=5, height=2)

btn_f1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # 상하좌우 다 늘리고 3씩 벌어지게 함
btn_f2.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f3.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f4.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

#clear줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_sum = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sum.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1 시작줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # rowspan = 현재 위치에서 아래쪽으로 x줄을 더함

# 0 시작줄
btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # columnspan = 현재 위치로부터 오른쪽으로 x줄을 더함
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)
root.mainloop()