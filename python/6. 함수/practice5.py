# 지역변수 / 전역변수
# 해당 스코프에서 사용할 수 있음 : 지역 변수
# 어디서든 사용 할 수 있음 : 전역 변수

gun = 10

def checkpoint(soldiers):
    #함수 내부에서 만들어진 지역변수 gun/ 초기화가 되지 않았다.
    # gun = 20 과 같이 초기화 가능, 그러나 외부 gun을 사용해야 함
    # 따라서 global 키워드를 사용한다.
    global gun #함수 외부 gun 변수를 가져온다. (전역)
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    # 이와 같이 사용하면, 함수 외부 변수를 사용할 수 있다.
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))