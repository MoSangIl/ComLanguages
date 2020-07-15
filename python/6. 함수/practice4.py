# 가변인자.

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # end=" " 해당 print 문에 이어서 출력한다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 23, "Python", "java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")


# 함수에 인자가 들어갈수도 들어가지 않을 수도 있을대 가변 인자를 사용

def profile_fake(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile_fake("유재석", 23, "Python", "java", "C", "C++", "C#","asdf", "asdf")
profile_fake("김태호", 25, "Kotlin", "Swift")