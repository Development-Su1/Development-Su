# 클래스( 너무나도 중요한 개념)
# 국민 게임인 스타크래프트를 텍스트 버전으로 만들어보면서 클래스를 하나씩 파헤쳐보도록 하겠습니다. 

# 테란 종족을 선택하고 게임을 플레이 한다고 가정
# 테란의 가장 기본 유닛인 마린을 먼저 만들어보겠습니다. 마린은 총을 쏠 수 있는 군인임.
# 유닛의 이름, 체력, 공격력 정보를 각각의 변수에 저장하고 
# 유닛이 생성되었다는 내용과 함께 유닛의 정보를 출력하는 것까지 코드로 작성
name = "마린"    # 유닛의 이름
hp = 40     # 유닛의 체력
damage = 5    # 유닛의 공격력

print("{0} 유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}\n" .format(hp, damage)) 


# 다른 유닛인 탱크
# 이동을 하면서 공격하는 일반 모드도 있지만, 지상에 탱크를 고정시키고 공격하는 시즈모드로 바뀌게 되면 
# 공격 사정거리가 늘어나게 되고 공격력도 막강해집니다. 
tank_name = "탱크"
tank_hp = 150
tank_damage = 60

print("{0} 유닛이 생성되었습니다." .format(tank_name))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))


# 이 두 유닛을 데리고 공격을 한다고 가정해보겠습니다. 
# 공격을 하는 부분은 공통으로 처리할 수 있을 것 같으니 함수로 정의해보겠습니다. 
# 앞에서 작성한 코드에 이어서 다음 내용을 추가합니다.
# 공격 함수
def attack (name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력: {2}]" .format(name, location, damage))


# attack() 함수를 통해 마린과 탱크에게 1시 방향을 공격을 하도록 명령을 내려보겠습니다.
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)


# 그런데 만약 탱크를 하나 더 만들면 어떻게 될까요? 
# 앞에서 tank_를 붙인 tank_name, tank_hp, tank_damage 변수는 이미 썼으니까 
# 이번에는 tank2_ 라고 하여 tank2_name, tank2_hp, tank2_damage 라고 해볼 수 있겠네요. 
# 새로운 탱크를 추가한 전체 코드는 다음과 같습니다.
name = "마린"
hp = 10
damage = 5

print("{0} 유닛이 생성되었습니다." .format(name))
print("체력 : {0}, 공격력 : {1}\n" .format(hp, damage))

tank_name = "탱크"
tank_hp = 60
tank_damage = 150

print("{0} 유닛이 생성되었습니다." .format(tank_name))
print("체력 : {0}, 공격력 : {1}\n". format(tank_name, tank_damage))

tank2_name = "탱크2"
tank2_hp = 60
tank2_damage = 150

print("{0} 유닛이 생성되었습니다." .format(tank2_name))
print("체력 : {0}, 공격력 : {1}\n". format(tank2_name, tank2_damage))

def attack(name, location, damage):
    print("{0}: {1} 방향으로 적군을 공격합니다. [공격력: {2}]". format(name, location ,damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)


# 하지만 실제 게임에서는 서로 다른 종류의 유닛들이 최소 수십에서 많게는 수백개가 존재합니다. 
# 유닛마다 이렇게 서로 다른 정보(이름, 체력, 공격력 등) 를 관리하기에는 무리가 많이 따르겠지요.
# 이 때 필요한 것이 바로 클래스입니다.
# 클래스 내에서 정의되는 함수를 메소드 >> 다만 첫 번째 전달값 위치에는 self를 적어야 함.
# class 클래스명:
    # def 메소드1(self, 전달값1, 전달값2, ...):
        # 실행명령문1
        # 실행명령문2
        # ...
# Unit 이라는 이름으로 클래스를 정의하고 메소드를 하나 만드는데 이름은 __init__라고 합시다.
# self 를 적고 뒤에는 이름, 체력, 데미지에 해당하는 전달값들을 적어줍니다.
# self.변수명 = 값
# 이렇게 정의된 변수를 멤버변수라고 하는데, 클래스 내에서 사용할 수 있는 변수 정도로 이해하시면 됩니다. 
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name    # 멤버변수 name 에 전달값 name 저장
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력: {0}, 공격력: {1}\n". format(self.hp, self.damage))


# 클래스를 통해 객체를 생성할 때는 이런 형식으로 합니다.
# 변수명 = 클래스명(전달값1, 전달값2, ...) 전달값은 클래스의 __init__() 에 정의된 부분 중 self 를 제외한 값
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 60)


# [총정리]
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name   
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력: {0}, 공격력: {1}\n". format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 60)
