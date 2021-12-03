# 메소드

# 예제
# 공격을 할 수 있는 유닛만을 위한 새로운 클래스를 정의하고 이름은 AttackUnit 이라고 하겠습니다. 
# AttackUnit 은 Unit 클래스와 동일하게 __init__() 생성자에서 name, hp, damage 멤버 변수를 정의하는데 
# print() 를 통한 출력문은 따로 적지 않겠습니다.
class AttackUnit:
    def __init__ (self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


# 공격을 하는 동작을 위한 메소드를 만들겠습니다.
# 메소드 이름은 attack 으로 하고 전달값에는 self 다음에 공격 방향을 의미하는 location 을 정의하겠습니다.
# 유닛 이름과 공격력은 이미 클래스 객체의 멤버 변수로 정의되어 있기 때문에 자기 자신을 의미하는 self. 을 쓰고,
# 공격 방향은 명령을 받을 때마다 달라질 수 있으므로 멤버 변수가 아닌 전달값을 사용하기 위해
# self. 없이 쓴다는 점 주의해주셔야 합니다.
# 하나의 문장이 너무 길어서 한 줄에 표현하기 어렵거나 보기 좋게 두 줄 이상으로 나누고자 할 때는 
# 문장 끝에 역슬래시(\) 를 넣음으로써 다음 줄에서 계속하여 문장을 이어갈 수 있습니다.
def attack (self, location):    # 전달 받은 방향으로 공격
    print("{0}: {1}방향으로 적군을 공격합니다. [공격력: {2}]". format(self.name, location, self.damage))


# 공격을 받아서 피해를 입는 동작도 정의해보겠습니다. 
# 적군의 공격 유닛은 종류별로 다른 공격력을 가지며 상황에 따라 피해 데미지도 달라질 수 있으므로 
# damage 를 전달값으로 받겠습니다. 그리고 유닛이 현재 가지고 있는 체력 정보에서 데미지만큼 값을 빼줘야겠지요. 
# 그런데 만약 공격을 받은 후 남은 체력이 0 이하라면 아쉽지만 유닛은 파괴처리를 해야할 것입니다.
def damage(self, damage):    # damage 만큼 유닛 피해
    print("{0}: {1} 데미지를 입었습니다.". format(self.name, damage))    # 데미지 정보 출력
    self.hp -= damage    # 유닛의 체력에서 전달받은 damage 만큼 감소
    print("{0}: 현재 남은 체력은 {1}입니다.". format(self.name, self.hp))    # 남은 체력 출력
    if self.hp <= 0:   # 남은 체력이 0 이하이면?
        print("{0}: 파괴되었습니다.". format(self.name))   # 유닛 파괴 처리


# AttackUnit 의 객체를 만들고 메소드를 사용해보겠습니다.
# 파이어뱃을 하나 만들고 5시 방향으로 공격 명령을 내려보겠습니다.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")    # 5시 방향으로 공격 명령


# 공격을 하는 와중에 적군으로부터 피해를 입는다고 가정하고 25 만큼의 데미지로 2 번 공격 받도록 해보겠습니다.
firebat1.damage(25)    # 남은 체력 25
firebat1.damage(25)    # 남은 채력 0


# [총정리]
class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 공격 방향
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage): # damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남은 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# 파이어뱃 : 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 채력 0