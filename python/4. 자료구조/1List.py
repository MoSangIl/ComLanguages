# 리스트 []

# 지하철 칸별로 10 명, 20명, 30명
 
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

#
subway1 = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 타고 있는 지하철!
# 해당 원소 값의 index
print(subway1.index("조세호"))

# 하하 도 다음 칸에서 탐 
# 끝에 원소 추가하기 append
subway1.append("하하")
print(subway1)

# 정형돈을 유재석 / 조세호 사이에 태워봄
# 해당 인덱스에 원소 추가
subway1.insert(1, "정형돈") # 넣을 인덱스 값이 필요
print(subway1)

# 맨 뒤에 있는 사람 뺌
# 끝 인덱스 제거
print(subway1.pop())
print(subway1)

# 같은 이름의 사람이 몇명 있는지 확인
# 해당 원소 갯수 확인 count
subway1.append("유재석")
print(subway1)
print(subway1.count("유재석"))

# 정렬도 가능 sort
num_list = [5, 2, 3, 4, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능 reverse
num_list.reverse()
print(num_list)

# 모두 지우기 clear
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 
num_list1 = [5, 2, 3, 4, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 extend
num_list1.extend(mix_list)
print(num_list1)