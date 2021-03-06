# 다양한 출력 포맷!

## 빈 자리-빈 공간 / 오른쪽 정렬 / 총 10자리 확보

###   빈공간/ > 오른쪽 정렬 / 10 10자리 공간
print("{0: >10}".format(500))

## 양수일땐 + 표시, 음수일땐 - 표시

print("{0: >+10}".format(500))
print("{0: >-10}".format(-500)) # 음수는 + / - 상관없음

## 왼쪽 정렬 / 빈칸 _로 채움

print("{0:_<+10}".format(500))

## 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

print("{0:+,}".format(100000000000))

## 3자리 콤마, 부호 , 자릿수 확보
## 빈자리는 ^ 로 채우기
print("{0:^<+30,}".format(100000000))

## 소수점 출력하기
print("{0:f}".format(5/3))
### 소수점 특정 자리수 까지 / (반올림하여 표시)
print("{0:.2f}".format(5/3))

#### 순서
print("{0:^<+30,.2f}".format(1000000000000/3))
#-> 빈공간 대체 문자 / 정렬 / 부호 / 공간 / 콤마(3자리) / 소수점 표시

