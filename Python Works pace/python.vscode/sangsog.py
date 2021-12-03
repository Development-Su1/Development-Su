# 상속
# 상속은 일반적으로 자식이 부모로부터 재산을 물려받는 것을 의미하죠.
# 부상당한 유닛을 치료해주는 메딕이 그 대표적인 예입니다.

# 메딕과 같이 공격력이 없는 유닛은 AttackUnit 클래스로 생성하기에는 알맞지 않으니, 
# 이전에 만들었던 Unit 클래스를 다시 가져와보겠습니다. 
# AttackUnit 클래스에 공격력을 의미하는 damage 멤버 변수가 있으므로 
# Unit 클래스는 공격 가능 여부와 상관 없이 일반적인 유닛을 위한 클래스로 수정을 해보겠습니다.
class Unit:
    def __init__ (self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.". format(self.name))        
        print("체력: {0}, 공격력: {1}". format(self.hp, self.damage))


# 모든 유닛은 이름과 체력 정보는 가지기 때문에 name, hp 는 남겨두고 공격력인 damage 는 없애보겠습니다. 
# 코드를 간결하게 하기 위해 print() 부분도 제외하겠습니다.
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# Unit 클래스와 AttackUnit 클래스의 __init__() 생성자만 놓고 비교해보니 겹치는 부분이 있네요.
# 클래스에는 상속이라는 개념이 있어서 공통되는 부분은 코드를 중복으로 적지 않고도 재사용을 할 수 있습니다. 
# 클래스를 상속받을 때는 클래스 이름 뒤에 괄호를 적고 상속 받을 클래스 이름을 명시해주면 됩니다. 
# 그리고 이 때 두 클래스는 자식클래스와 부모클래스라고 표현합니다. 
# class 자식클래스(상속받을 부모클래스):
class AttackUnit(Unit):    # Unit 클래스를 상속
    def __init__(self, name, hp, damage):  
        Unit. __init__ (self, name, hp)     # 부모 클래스의 생성자 호출
        self.damage = damage


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
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 채력 0