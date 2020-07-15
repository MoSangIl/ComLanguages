#키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

# 함수 실행시에 인자에 인자명을 사용하면
# 순서에 상관없이 인자를 넣을 수 있다.
profile(age = 12, name = "모상일", main_lang = "Python")
profile(main_lang="java", age=234, name="asdg")