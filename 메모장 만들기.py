import os
import tkinter.messagebox as msgbox #메세지 박스용도
from tkinter import * #tkinter 활용

root = Tk()
root.title("제목 없음 - Windows 메모장") # 제목
root.geometry("640x480+400+100") # 크기

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일 있으면 true 없으면 false
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) #텍스트 삭제
            txt.insert(END, file.read()) # 불러오기

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)
def warn():
    msgbox.showwarning("경고", "저장하시겠습니까?") # 저장 경고 함수 생성


#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새로 만들기(N)")
menu_file.add_command(label="새 창(W)")
menu_file.add_command(label="열기(O)", command=open_file) # 열기 함수 불러오기
menu_file.add_command(label="저장(S)", command=save_file) # 저장 함수 불러오기
menu_file.add_command(label="다른 이름으로 저장(A)...")
menu_file.add_separator() # 칸 나누기
menu_file.add_command(label="페이지 설정(U)")
menu_file.add_command(label="인쇄(P)...")
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)


# 편집 메뉴
menu_edt = Menu(menu, tearoff=0)
menu_edt.add_command(label="실행 취소(U)")
menu_edt.add_separator()
menu_edt.add_command(label="잘라내기(T)")
menu_edt.add_command(label="복사(C)")
menu_edt.add_command(label="붙여넣기(P)")
menu_edt.add_command(label="삭제(L)")
menu_edt.add_separator()
menu_edt.add_command(label="Bing으로 검색(S)...")
menu_edt.add_command(label="찾기(F)")
menu_edt.add_command(label="다음찾기(N)")
menu_edt.add_command(label="이전찾기(V)")
menu_edt.add_command(label="바꾸기(R)")
menu_edt.add_command(label="이동(G)...")
menu_edt.add_separator()
menu_edt.add_command(label="모두 선택(A)")
menu_edt.add_command(label="시간/날짜(D)")
menu.add_cascade(label="편집(E)", menu=menu_edt)

# 서식 메뉴
menu_form = Menu(menu, tearoff=0)
menu_form.add_checkbutton(label="자동 줄 바꿈(W)")
menu_form.add_command(label="글꼴(F)...")
menu.add_cascade(label="서식(O)", menu=menu_form)

# 보기 메뉴

menu_view = Menu(menu, tearoff=0)
menu_view.add_command(label="확대하기/축소하기")
menu_view.add_checkbutton(label="상태 표시줄(S)")
menu.add_cascade(label="보기(V)", menu=menu_view)

# 도움말 메뉴

menu_help = Menu(menu, tearoff=0)
menu_help.add_command(label="도움말 보기(H)")
menu_help.add_command(label="피드백 보내기(F)")
menu_help.add_separator()
menu_help.add_command(label="메모장 정보(A)")
menu.add_cascade(label="도움말(H)", menu=menu_help)
root.config(menu=menu)


# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview) 
txt = Text(root)
txt.pack(side="left", fill="both", expand=True) # 화면에 꽉 차게

root.mainloop()