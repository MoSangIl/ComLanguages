# 대기 손님의 치킨 요리시간을 줄이고자 자동 주문 시스템을 제작
# 시스템 코드 확인 및 적절한 예외처리 넣어라

# 조건 1: 1 보다 작거나 숫자가 아닌 입력값은 ValueError 로 처리
#         메세지: "잘못된 값을 입력하였습니다."
# 조건 2: 대기 손님 주문 가능한 총 치킨량 10마리로 한정
#         메세지: "재고가 소진되어 더 이상 주문을 받지 않습니다."

class NoMoreChicken(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 # 홈 - 만석 / 대기 번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까? "))
        if order <= 0:
            raise ValueError
        elif order > chicken: 
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting+=1
            chicken -= order
        if chicken == 0:
            raise NoMoreChicken("재고가 소진되어 더 이상 주문을 받지 않습니다.") 
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except NoMoreChicken as err:
        print(err)
        break