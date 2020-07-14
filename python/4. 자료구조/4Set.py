# Set {}
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3} 중복 허용 안함

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 자바와 파이썬 모두 가능 (교집합)
print(java & python)
print(java.intersection(python))

# 자바 혹은 파이썬을 하는 개발자 (합집합)
print(java | python)
print(java.union(python))

# 자바 가능 하지만 파이썬 못함 (차집합)
print(java - python)
print(java.difference(python))

# python 가능 해짐-> 추가하기
python.add("김태호")
print(python)

# Java 가먹음 -> 제외하기
java.remove("김태호")
print(java)