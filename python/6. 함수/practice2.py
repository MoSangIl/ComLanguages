# 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "python")
profile("김태호", 25, "java")

# 같은 학교 같은 학년 같은 반 같은 수업..

## 함수 인자에 초기 값을 넣어서 사용 할 수 있다.
def profile_(name, age=17, main_lang="Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile_("유재석")
profile_("모상일")