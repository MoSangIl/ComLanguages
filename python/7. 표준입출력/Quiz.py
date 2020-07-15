# Quiz

# 매주 1회 작성해야하는 보고서
# 항상 아래와 같은 형태로 출력되어야 한다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1 ~ 50 주차까지의 보고서 파일 만드는 프로그램

# 조건 : 파일명은 1주차.txt... 

for week in range(1, 51):
    with open("7. 표준입출력/" + str(week)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- " + str(week) + " 주차 주간보고 -\n")
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 :")
