# 메소드 오버라이딩
# 부모 클래스에 정의된 메소드를 그대로 사용하지 않고 자식 클래스에서 같은 이름으로 메소드를 새롭게 정의하여 사용함.

# 지상 유닛을 위한 이동 속도를 의미하는 speed 를 Unit 클래스에 추가해보겠습니다. 
# 그리고 이동을 위한 move() 메소드도 새롭게 정의하고 구분을 위해
# [지상 유닛 이동] 이라는 문구와 함께 어떤 유닛이 몇 시 방향으로 이동하는지를 출력하겠습니다.
class Unit:
    def __init__ (self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed    # 지상 이동 속도

    def move (self, location):    # 이동 함수 정의
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도: {2}]". format(self.name, location, self.speed))


# 공격 유닛인 AttackUnit 클래스에 speed 를 추가하겠습니다.
class AttackUnit(Unit):
      def __init__ (self, name, hp, speed, damage):   # speed 추가
          Unit. __init__ (self, name, hp, speed)    # speed 추가
          self.damage = damage


# AttackUnit 클래스를 상속받는 공중 공격 유닛인 FlyableAttackUnit 클래스도 수정을 하겠습니다.
# 공중 공격 유닛의 경우 공중 이동 속도인 flying_speed 가 이미 정의되어 있으며 지상으로는 이동하지 못하기 때문에 
# 지상 이동 속도는 그냥 0 으로 설정을 해주겠습니다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__ (self, name, hp, damage, flying_speed):
        AttackUnit. __init__ (self, name, hp, 0 ,damage)    # 지상 speed는 0
        Flyable. __init__ (self, flying_speed)


# 수정이 잘 되었는지 확인하기 위해 지상 이동 속도를 포함한 새로운 공격 유닛을 만들어보겠습니다. 
# 이번에 만들 유닛은 스타크래프트에서 가장 속도가 빠른 기동성 최강의 유닛인 벌쳐입니다.
# 체력 80, 이동 속도 10, 공격력 20 
vulture = AttackUnit("벌쳐", 80, 10, 20)   # 지상 speed 10


# FlyableAttackUnit 도 수정을 하였으므로 공중 공격 유닛도 하나 만들어볼게요. 
# 이번에는 테란 유닛 중 가장 강력한 거대 우주 함선으로 압도적인 화력을 자랑하는 배틀크루저를 만들겠습니다.
battlecruiser = FlyableAttackUnit("배틀크루저", 100, 70, 50)


# 이제 앞에서 만든 벌쳐와 배틀크루저를 함께 이동시켜보겠습니다. 
# 지상 유닛인 벌쳐는 move() 를 이용할 수 있고 공중 유닛은 배틀크루저는 fly() 를 이용하면 되겠네요.
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "11시")


# 스타크래프트에는 굉장히 많은 지상 유닛과 공중 유닛이 있는데 이들을 이동시킬 때마다
# 지상 유닛인지 공중 유닛인지를 구분하여 move() 와 fly() 를 적기에는 너무 번거로울 것 같습니다. 
# 그리고 fly() 를 이용할때는 유닛의 이름정보까지 전달해야하는 불편함도 있지요.
# 이런 경우에 우리는 메소드 오버라이딩을 이용할 수 있습니다.
# Unit 클래스에 정의된 move() 메소드를 FlyableAttackUnit 클래스 내에서 오버라이딩 해보겠습니다. 
# 메소드 오버라이딩은 부모 클래스에 정의된 메소드를 그대로 자식 클래스에서 동일한 이름과 전달값으로 하여 정의함.
# 대신 메소드 동작만 원하는대로 변경하면 됨.
# 공중 공격 유닛의 이동이므로 [공중 유닛 이동] 이라는 문구를 출력하고 실제 이동은 공중으로 날아다녀야 하므로 
# 또다른 부모 클래스인 Flyable 에 정의된 fly() 메소드를 호출하는 것으로 하겠습니다. 
# 이 때 유닛 이름과 이동할 위치 정보를 함께 전달합니다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__ (self, name, hp, damage, flying_speed):
        AttackUnit. __init__ (self, name, hp, 0, damage)
        Flyable. __init__ (self, flying_speed)

    def move (self, location):    # Unit 클래스의 move() 메소드를 새롭게 정의 (오버라이딩)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 이번에는 지상, 공중 구분 없이 모두 move() 로만 이동하겠습니다. 
vulture. move("11시")
battlecruiser.move("9시")    # 오버라이딩된 move() 호출

# 공중 공격 유닛인 FlyableAttackUnit 은 지상 이동이 아닌 공중 이동을 해야 하므로 
# Flyable 클래스의 fly() 를 쓰고 있었는데 유닛이 많아지면 관리가 어려우므로 move() 를 재정의하여 
# 메소드 내에서 fly() 를 호출하도록 하였습니다. 이렇게 하면 유닛별로 같은 move() 를 호출하더라도 
# AttackUnit 을 통해 만들어진 유닛은 부모 클래스인 Unit 의 move()를, FlyableAttackUnit 을 통해 만들어진 유닛은 
# 오버라이딩을 통해 새롭게 정의된 FlyableAttackUnit 의 move() 를 호출하게 됩니다.


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

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # 오버라이딩된 move() 호출