# With

import pickle

## 파일을 열어서 변수로 저장하고, 내용을 실행한다.
## 따라서 알아서 종료 됨!
with open("7. 표준입출력/profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("7. 표준입출력/study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("7. 표준입출력/study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())