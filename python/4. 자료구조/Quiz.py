# Quiz -> 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰!

## 조건 1: 편의상 댓글은 20명이 작성 / 아이디는 1~20이라고 가정
## 조건 2: 댓글 내용과 상관없이 무작위로 추첨 / 중복 불과
## 조건 3: random 모듈의 shuffle과 sample을 활용

# 출력
# --- 당첨자 발표 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --- 축하합니다 ---

 # 활용 예제
# from random import *
# lst = [1, 2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst) 
# print(sample(lst, 1))

from random import *
# 조건 1
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
## users = range(1, 21) -> type = range
## 따라서, users = list(users)

# 조건 2
shuffle(ids)
chicken_get_person = sample(ids, 1)
ids.remove(chicken_get_person[0])
coffee_get_people = sample(ids, 3)
## shuffle(users)
## winners = sample(users, 4)

# 출력
print("--- 당첨자 발표 ---")
print("치킨 당첨자: %d" % chicken_get_person[0])
print("커피 당첨자 :", coffee_get_people)
print("--- 축하합니다 ---")

## print("커피 당첨자 : {0}".format(users[1:]))
## format을 사용하면 리스트도 문자열과 출력할 수 있다.