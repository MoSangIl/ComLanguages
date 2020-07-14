# 문자열 포맷
# + / , 이외의 문자열을 조작하는 방법

# 방법 1 %
#print("나는 20살입니다.")
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % 'A')
## %s
print("나는 %s살입니다." % 23)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2 .format
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3 
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

# 방법 4 (v3.6 이상 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")