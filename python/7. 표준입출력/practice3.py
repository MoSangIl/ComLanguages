# 파일 입출력

# 열 파일 이름 / 접근 지정자 / 인코딩 
## w -> 쓰기(덮어씀)
score_file = open("7. 표준입출력/score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

## a -> 쓰기(이어씀)
score_file1 = open("7. 표준입출력/score.txt", "a", encoding="utf8")
score_file1.write("과학 : 50\n")
score_file1.write("코딩 : 100")
score_file1.close()

## r -> 읽기
# -- #
score_file_r = open("7. 표준입출력/score.txt", "r", encoding="utf8")
print(score_file_r.read())
score_file_r.close()

# -- #
score_file_r1 = open("7. 표준입출력/score.txt", "r", encoding="utf8")
print(score_file_r1.readline())
print(score_file_r1.readline())
print(score_file_r1.readline())
print(score_file_r1.readline())
score_file_r1.close()

# -- #
score_file_read = open("7. 표준입출력/score.txt", "r", encoding="utf8")
while True:
    line = score_file_read.readline()
    if not line:
        break
    print(line)
score_file_read.close()

### List 사용

score_file_list = open("7. 표준입출력/score.txt", "r", encoding="utf8")
lines = score_file_list.readlines()
for line in lines:
    print(line)
score_file_list.close()
