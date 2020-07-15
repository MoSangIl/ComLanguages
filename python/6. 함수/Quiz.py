# Quiz

# 표준 체중을 구하는 프로그램

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시ㅓ

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def calculate_stdWeight(height, gender):
    if gender == "남자":
        std_weight = height * height * 22
    elif gender == "여자":
        std_weight = height * height * 21
    else:
        print("오류")
        return -1
    return std_weight

gender = input("성별을 입력해주세요.(남자, 여자): ")
height = float(input("키를 입력해주세요(단위: m): "))

std_weight = calculate_stdWeight(height, gender)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다."\
    .format(height * 100, gender, round(std_weight * 100) / 100))

# round(number, 2) -> 소수점 둘째자리까지 반올림

