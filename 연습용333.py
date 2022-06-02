from pickle import LIST
from platform import python_branch


subway = [10, 20, 30]
print(subway)

subway = ["유찬홍", "조병진", "박준수"]
print(subway)

#병진이는 몇 번쨰 칸에 타고 있을까?
print(subway.index("조병진"))

#정호가 다음 정류장에서 다음칸에 탐
subway.append("이정호")
print(subway) 

#정호를 병진이랑 준수 사이에 태워보았다.
subway.insert(1, "이정호")
print(subway)

#뒤에서 한명씩 하차
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유찬홍")
print(subway)
print(subway.count("유찬" +"홍"))

#정렬
list = [5, 2, 4, 3, 1]
list.sort()
print(list)

#뒤집기
list.reverse()
print(list)

#모두지우기
list.clear
print(list)

#다양한 자료형을 함께 쓴다면?
list = [5, 2, 4, 3, 1]
mix_list = ["조병진", 20, True]
print(mix_list)

#리스트 확장
list.extend(mix_list)
print(list)

cabinet = {3:"조병진", 100:"유찬홍", 8888888:"김세현"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(5))#대괄호는 오류뜨고 get은 None을 출력함
print(cabinet.get(5,"사용 가능"))
print(3 in cabinet) #True 출력
print(5 in cabinet) #False 출력
#새로운 값 추가
print(cabinet)
cabinet[9] = "박준수"
print(cabinet)
#삭제
del cabinet[8888888]
print(cabinet)
#지금 있는 key들만 출력
print(cabinet.keys())

#지금 있는 value만 출력
print(cabinet.values())

#쌍으로 둘다출력
print(cabinet.items())

#모든 값 삭제
cabinet.clear()
print(cabinet)

#튜플
menu =  ("돈가스", "치즈가스")
print(menu[0]) #돈가스 출력
print(menu[1]) # 치즈가스 출력
#튜플은 값을 추가나 변경할수 없음

(name, age, hobby) = ("유찬홍", 16, "롤")
print(age) #값을 뽑아쓸수있음

#집합(set), 중복이 안되고 순서가 없음
a={1, 2, 3, 3, 3}
print(a)

java = {"유찬홍", "최성현", "이정호"}
python = set(["유찬홍", "김연우"])

#교집합 (자바랑 파이썬 다되는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (자바를 할수 있거나 파이썬을 할수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (자바는 되는데 파이썬이 안되는 개발자)
print(java - python)
print(java.difference(python))

#파이썬 개발자 추가
python.add("이정호")
print(python)

#자바를 까먹어버림
java.remove("이정호")
print(java)

weather = input("오늘 날씨가 어때요?")#input=scanf
if weather == "비" or weather == "눈": #or = ||
    print("우산을 챙기세요")
elif weather == "미세먼지":#파이썬에서는 if문 뒤에 콜론을 쓴다
    print("마스크")
else:
    print("뭐 필요한거 없음")

temp = int(input("밖에 기온이 어때요? ")) #정수형으로 입력받기
if 30 <= temp:
    print("집에서 쉬어라")
elif 10<=temp and temp < 30: #and=&& 근데 여기서는 10<temp<30 이런거 가능함
    print("외출 ㄱㄱ")
elif 0 <= temp <10:
    print("따뜻하게 입고 가자")
else:
    print("걍 나가지 마라")

for wait_num in range(6): #파이썬식 for문
    print("대기번호: {0}".format(wait_num))
