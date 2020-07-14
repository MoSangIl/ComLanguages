# 문자열 처리 함수
python = "Python is Amazing"

# 소문자로 변경 lower
print(python.lower())

# 대문자로 변경 upper
print(python.upper())

# 대문자인가? isupper
print(python[0].isupper())

# 문자열길이 len
print(len(python))

# 문자열 대체 replace
print(python.replace("Python", "Java"))

# 인덱스 값 확인 index
index = python.index("n")
print(index) # 첫번재 n
index = python.index("n", index + 1) # 시작 위치 지정!
print(index) # 두번째 n

# 인덱스 값 확인 find! 
# index 와 다르게 find는 원하는 값이 없을때 예외처리 한다. (-1)
print(python.find("Java"))
print("hi")

# 해당 문자열 등장하는 횟수 count
print(python.count("n"))