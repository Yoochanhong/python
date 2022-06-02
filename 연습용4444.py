#자료구조 변경

menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

#이벤트 당첨 프로그램
#1명은 치킨, 3명은 커피쿠폰
#댓글은 20명으로 생각하고 아이디는 각자 1~20이라고 가정
#걍 무작위, 중복 안됨
#random 모듈의 shuffle과 sample를 활용
from random import *
users = range(1, 21) #1부터 21 직전까지 숫자 생성
users = list(users)
shuffle(users)

winners = sample(users, 4) #1명은 치킨, 3명은 커피 당첨

print(" -- 당첨자 발표-- ")
print("치킨 당첨자 : {0}번".format(winners[0]))
print("커피 당첨자 : {0)".format(winners[1:]))
print(" -- 축하합니다 -- ")

