# 에러 만들기! raise
# 원하지 않는 패스 차단

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번재 숫자를 입력하세요 : "))
    num2 = int(input("두 번재 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요")