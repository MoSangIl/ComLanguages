# 클래스

## 스타크래프트 예제

# #마린  : 공격 유닛, 군인. 총을 쏨
# name = "마린"
# hp = 40     # 체력
# damage = 5  # 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포 쏨 (일반모드 / 시즈 모드)
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력: {2}]"\
#         .format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

### Unit Class 생성

class Unit:
    # init 함수
    def __init__(self, name, hp, damage):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

class AttackUnit:
    # init 함수
    def __init__(self, name, hp, damage):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력: {2}]"\
        .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

marine1 = Unit("마린", 40, 5)
marine1 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중, 비행기, 클로킹 스킬
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True ## 외부에서 해당 객체에만 변수를 생성할 수 있다. / wraith1 에는 적용 X

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# 파이어 뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
