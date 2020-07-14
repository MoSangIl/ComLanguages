# 문자열 생성 방법
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년 이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "981230-1333333"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 0, 1
print("월 : " + jumin[2:4]) # 2부터 4 직전까지 2, 3
print("일 : " + jumin[4:6]) # 4부터 6 직전가지 4, 5

print("생년월일 : " + jumin[:6]) # [0:6] or [:6] 
print("뒤 7자리 : " + jumin[7:]) # [7:13] or [7:]
# 맨 뒤에서 7번재부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])