# 상속 

class Unit:
    # init 함수
    def __init__(self, name, hp):
        # 멤버 변수
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}\n".format(self.hp))

## 상속시에 (상속할 클래스)
class AttackUnit(Unit):
    # init 함수
    def __init__(self, name, hp, damage):
        # (init 함수 호출)
        Unit.__init__(self, name, hp)
        # 멤버 변수
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

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

### 다중 상속
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공격, 비행 둘다 가능
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyre = FlyableAttackUnit("발키리", 200, 6, 5)
valkyre.fly(valkyre.name, "3시")
valkyre.attack("3시")