# 코코아 서비스 이용 택시 기사
# 50명의 승객과 매칭 기회 시, 총 탑승 승객 수를 구하는 프로그램

## 조건 1: 승객 별 운행 소요 시간 5 ~ 50 분 사이 난수
## 조건 2: 소요 시간 5 ~ 15분 사이의 승객만 매칭

from random import *

matched_customer = 0 # 총 탑승 승객 수
for customer in range(1, 51):
    time = randint(5, 50) # 5 ~ 50 / randrange(5, 50) -> 5 ~ 490
    if 5 <= time <= 15:
        print("[O]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        matched_customer += 1
    else:
        print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print(f"총 탑승 승객 : {matched_customer} 분")
