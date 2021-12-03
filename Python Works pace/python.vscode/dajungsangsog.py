# 다중상속

# 공중 유닛의 경우 하늘을 날아서 이동하는데 이 기능은 지상 유닛에는 적용될 수 없는 내용이므로 
# 날 수 있는 기능을 정의하는 클래스를 별도로 하나 만들겠습니다. 
# 클래스 이름은 Flyable 이라 하고 __init__() 생성자에는 날아서 이동할 때의 속도를 의미하는 flying_speed를 멤버변수로 두겠습니다.
# 그리고 실제로 이동하는 동작을 fly() 함수에 정의할텐데, 
# Flyable 클래스는 날아서 이동하는 기능만 제공하므로 어떤 유닛인지에 대한 정보는 따로 가지지 않도록 하겠습니다.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__ (self, flying_spead):    # 공중 이동 속도
        self.flying_spead = flying_spead

    def fly(self, name, location):    # 유닛 이름, 이동 방향
         print("{0}: {1} 방향으로 날아갑니다. [속도: {2}]". format(name, location, self.flying_spead))


# 공중 공격 유닛을 위한 새로운 클래스를 만들어보겠습니다. 
# 공격 유닛인 AttackUnit과 "공중", 하늘을 날 수 있는 기능을 제공해주는 Flyable 클래스를 조합하면 공중 공격 유닛을 만들 수 있다.
# 이름은 FlyableAttackUnit 으로 하고, 이번에는 AttackUnit 과 Flyable 클래스를 함께 상속받도록 하겠습니다. 
# 이렇게 2개 이상의 클래스를 상속받는 것을 다중 상속이라고 표현하며 형태는 
# class 자식클래스(부모클래스1, 부모클래스2, ...):
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__ (self, name, hp, damage, flying_spead):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, name, flying_spead)


# 발키리라는 유닛을 하나 만들어보겠습니다.
# FlyableAttackUnit 클래스로부터 새로운 객체를 만들고 이름은 valkyrie 로 하겠습니다.
valkyrie = FlyableAttackUnit("발키리", 200, 10, 9)
valkyrie.fly(valkyrie.name, "3시")    # 3시 방향으로 발키리를 이동


# [총정리]
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
    def __init__(self, flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed

    def fly(self, name, location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self, name, hp, damage) # 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed) # 공중 이동 속도

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동 속도
valkyrie.fly(valkyrie.name, "3시") # 3시 방향으로 발키리를 이동