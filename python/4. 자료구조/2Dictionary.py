# Dictionary {}
## Key 에 대한 중복이 허락 되지 않는다.

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # key값을 넣어 내용을 가져온다.
print(cabinet[100])

# get -> Key를 잘못 접근 했을 경우 예외처리를 한다. 
# Key 값에 직접 접근하는 것과 차이!
print(cabinet.get(3))
# 비었을 경우 예외로 사용할 텍스트를 받는다.
print(cabinet.get(5, "사용가능"))

# Key 값 여부를 판단 in
print( 3 in cabinet) # True
print( 5 in cabinet) # False

####
hotel = {"A-3":"유재석", "B-100" : "김태호"}
print(hotel["A-3"])
print(hotel["B-100"])

# 추가하기 
print(hotel)
hotel["A-3"] = "김종국" # value 대체
hotel["C-20"] = "조세호" # key & value 추가
print(hotel)

# 삭제하기 del
del hotel["A-3"]
print(hotel)

# Key 만 출력하기
print(hotel.keys())

# Value 만 출력
print(hotel.values())

# key, Value 쌍으로 출력
print(hotel.items())

# hotel 폐점
hotel.clear()
print(hotel)