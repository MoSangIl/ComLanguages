#Pickle
## 프로그램 상에서 데이터를 파일로 저장하는 것

import pickle
# wb -> binary
profile_file = open("7. 표준입출력/profile.pickle", "wb")
profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

## Read
profile_file_r = open("7. 표준입출력/profile.pickle", "rb")
profile_r = pickle.load(profile_file_r)
print(profile_r)
profile_file_r.close

### 정리
## 피클에 저장한 내용을 변수로 저장. 
## 아마 이진으로 저장하는 듯