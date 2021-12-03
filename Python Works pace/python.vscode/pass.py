# 패스
# 건물을 위한 클래스를 하나 만들어 보겠습니다. 
# 건물도 일반 유닛처럼 이름과 체력이 있는데 적군으로부터 공격을 받으면 파괴될 수가 있습니다. 
# Unit 클래스에 공통 속성이 있으니 이를 상속 받아서 만들도록 하구요.
#  __init__() 생성자의 세부 내용은 일단은 그냥 내버려 두겠습니다. 
# 다른 작업을 먼저 하고 나서 나중에 코드를 완성한다고 가정할게요. 이럴 때 파이썬에서는 pass 를 쓸 수 있습니다.
# 이것은 아무것도 하지 않고 일단은 그냥 넘어간다는 의미로 사용됩니다. 
# 즉, __init__() 생성자는 실제로는 완성되지 않았지만 마치 완성된 것처럼 보여질 수 있는 것이죠.
class buildingUnit(Unit):
    def __init__ (self, name, hp, location):
        pass

supply_depot = buildingUnit("서플라이 디폿", 500, "7시")


# pass 는 다른 곳에서도 사용이 가능합니다. 위 코드에 이어서 함수를 2개 만들어볼게요. 
# 게임 시작을 알리는 game_start() 함수와 게임 종료를 알리는 game_over() 함수입니다. 
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
# game_start() 함수에서는 정의된 동작을 수행하고 game_over() 함수에서는 pass 를 통해 그냥 넘어가게 된 것이죠.


# [총정리]
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]". format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]". format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]". format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()