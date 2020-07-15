# 표준입출력

# sep -> , 로 연결된 문자열 사이에 들어감
print("Python", "Java", "JavaScript", sep=" vs ")

# end ->  해당 문자열을 출력하고, 해당 줄에 이어 쓴다.
print("Python", "Java",  sep=", ", end="?")
print("무엇이 더 재밌을까요")

import sys

# 표준 출력
print("Python", "Java", file=sys.stdout)
# 표준 에러 출력
print("Python", "Java", file=sys.stderr)

###
scores = {"수학": 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    # ljust(n) -> n칸 공간 확보, 왼쪽 정렬 
    print(subject.ljust(8), score)
    # rjust(n) -> n칸 공간 확보, 오른쪽 정렬
    print(subject, str(score).rjust(4), sep=":")


###
for num in range(1, 21):
    #zfill(3)-> 3칸 확보 및 빈 공간 zero 로 대체
    print("대기번호 : " + str(num).zfill(3))
# 001
# 002
# 003
# 004
# ...
###
# 표준 입출력
## input 은 문자열로 입력 받는다. 
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")