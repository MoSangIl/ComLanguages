# Pass
class Unit:
    # init 함수
    def __init__(self, name, hp, speed):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}\n".format(self.hp))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

## 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass #일단은 넘어간다. 
        ## super 이용 / self사용 할 필요 없음
        ## 다중상속시에는 상속 클래스중 첫번째 만 적용됨.. 따라서 하나씩이용해주어야 함
        super().__init__(name, hp, 0)
        self.location = location

# 서플라이
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
# 실행은 됨.