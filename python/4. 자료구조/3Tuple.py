# Tuple ()
## List와 동일하나 속도가 빠르다
## 값은 고정되어 사용 된다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# add를 사용할 수 없음
## -> 값 추가 및 변경 불가

name = "모상일"
age = 23
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("모모모", 23, "ggg")
print(name, age, hobby)