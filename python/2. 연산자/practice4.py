#랜덤 함수
## 랜덤 라이브러리

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의 정수 생성
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 10))
#
print(" random 1~10 정수")
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의 정수
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)
print(int(random() * 10) + 1)

print(" random 1~23 정수")
print(int(random() * 23) + 1) # 1 ~ 23 이하의 임의 정수
print(int(random() * 23) + 1)
print(int(random() * 23) + 1)
print(int(random() * 23) + 1)
print(int(random() * 23) + 1)

print(" randrange(1, 46) -? 1 ~ 46 미만 임의 정수 ")
print(randrange(1, 46)) # 1 ~ 45
print(randrange(1, 46))

print(" randint(1, 46) -? 1 ~ 46 이하 임의 정수 ")
print(randint(1, 46)) # 1 ~ 46
print(randint(1, 46))