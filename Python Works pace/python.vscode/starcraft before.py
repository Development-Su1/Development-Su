# 스타그래프트 전반전
# 가장 기본이 되는 Unit 클래스부터 먼저 보겠습니다. 
# 스타크래프트에서는 유닛이 생성될 때마다 각 유닛의 고유한 소리를 통해 생성되었음을 알려줍니다.
# 우리 코드에서는 소리 대신 __init__() 생성자에 print() 를 추가하여 어떤 유닛이 생성되었는지를 출력하도록 하겠습니다.
# move() 메소드에서는 유닛 이동 관련하여 2번이나 출력하게 되어 있으므로 처음 출력문인 [지상 유닛 이동] 문구는 제외함.
# 기존에 공격유닛인 AttackUnit 클래스를 만들면서 적군으로부터 공격을 받을 때 호출되는 damaged() 메소드를 정의하였는데 
# 공격을 할 수 없는 일반 유닛도 공격을 받을 수 있기 때문에 이 메소드는 Unit 클래스로 이동을 하고 
# AttackUnit 클래스에서는 제외하도록 하겠습니다.
class Unit:
    def __init__ (self, name, hp, speed):
        self. name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.". format(self.name))

    def move (self, location):
        print("{0}: {1}방향으로 이동합니다. [속도: {2}]". format(self.name, location, self.speed))

    def damaged (self, damage):
        print("{0}: {1} 데미지를 입었습니다.". format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.". format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.". format(self.name))


# AttackUnit 클래스인데 Unit 클래스로 damaged() 메소드를 이동한 것 외에는 따로 수정하지 않겠습니다.
class AttackUnit (Unit):
    def __init__ (self, name, hp, speed, damage):
        Unit.__init__ (self, name, hp, speed)
        self.damage = damage

    def attack (self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력: {2}]". format(self.name, location, self.damage))     


# 마린 공격 유닛 생성 (각 유닛에 대한 클래스를 직접 정의)
# 마린은 스팀팩(stimpack)이라는 특수 기술이 있는데 이 기술을 사용하게 되면 일정 시간 동안 이동 및 공격 속도를 
# 아주 빠르게 증가시킬 수 있습니다. 대신 자기 자신의 체력이 10 만큼 소모되기 때문에 
# 현재 남은 체력이 10 보다 클 때만 사용할 수 있다는 조건이 필요합니다. 
# stimpack() 이라는 메소드를 만들고 체력이 10 보다 크면 체력 10 소모 후 스팀팩 사용 문구 출력, 
# 10보다 작으면 사용 불가하다는 문구 출력을 하도록 하겠습니다.  
class Marine (AttackUnit):
    def __init__ (self):
        AttackUnit.__init__ (self, "마린", 40, 1, 5)    # 이름, 체력, 이동속도, 공격력

    def stimpack (self):
        if self.hp > 10:
            self.hp -= 10    # 체력 10 소모
            print("{0}: 스팀팩 사용합니다. (hp 10감소)". format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용할 수 없습니다.". format(self.name))   


# 탱크를 위한 Tank 클래스
# 탱크는 특수 기술로 시즈(siege)모드가 있는데 이 기술을 사용하면 지상에 탱크를 고정시켜서 무려 2배에 달하는 공격력, 
# 더 넓은 사정거리로 공격이 가능합니다. 
# 다만, 이 기술은 처음부터 바로 사용할 수 없고 업그레이드를 통한 시즈모드 개발을 완료해야만 사용 가능하다.
# 모든 탱크가 시즈모드로 전환할 수 있게 됩는데 이미 만들어진 탱크도, 앞으로 만들어질 탱크도 모두 포함이다.
# 어떤 클래스로부터 만들어진 객체에 일괄적으로 뭔가를 적용하려면 멤버변수가 아닌 클래스 변수로 선언할 수 있습니다. 
class tank (AttackUnit):
    siege_developed = False   # 시즈모드 개발여부


# 클래스 변수는 클래스 이름과 함께 어디서든지 사용 가능합니다. 
# Tank.siege_developed 라고 하면 탱크 클래스 변수의 값에 직접 접근하여 시즈모드 개발이 완료되었는지를 확인할 수 있음. 
# 멤버변수가 각 클래스 객체마다 다른 값을 가진다면 클래스 변수는 모든 객체가 동일한 값을 가진다는 점이 다릅니다.
# 시즈모드 개발이 완료되었다고 해서 모든 탱크가 시즈모드를 항상 해야하는 것은 아니므로 
# 시즈모드 여부를 확인하기 위해 siege_mode 라는 멤버변수를 정의합니다. 
# 처음에는 일반모드일 테니 시즈모드를 해제 상태로, 즉 False 로 두겠습니다.    
class tank(AttackUnit):
    def __init__ (self):
        AttackUnit.__init__ (self, "탱크", 100, 60, 1, 70)
        self.siege_mode = False


# 시즈모드와 일반모드를 전환하기 위한 set_siege_mode() 메소드를 정의합니다.
# 일반모드인 경우는 시즈모드로, 시즈모드인 경우는 일반모드로 전환합니다. 
class tank (AttackUnit):
    # 시즈모드
    def set_siege_mode(self):
        if tank.siege_developed == False:    # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return 

    # 현재 시즈모드가 아닐 때 
        if self.siege_mode == False:
            print("{0}: 시즈모드로 전환합니다.". format(self.name))
            self.damage *= 2
            self.siege_mode = True    # 시즈 모드 설정

    # 현재 시즈모드일 때
        else:
            print("{0}: 시즈모드를 해제합니다.". format(self.name))
            self.damage /= 2    # 공격력 절반으로 감소
            self.siege_mode = False    # 시즈 모드 해제   


# 공중 유닛을 위해 만들었던 Flyable 클래스와 공중 공격 유닛을 위한 FlyableAttackUnit 클래스를 가져와서 사용하겠습니다.
class Flyable:
    def __init__ (self, Flying_speed):
        self.Flying_speed = Flying_speed

    def fly(self, name ,location):
        print("{0}: {1} 방향으로 날아갑니다. [속도: {2}]". format(name, location, self.Flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__ (self, name, hp, damage ,Flying_speed,):
        AttackUnit.__init__ (self, name, hp, damage ,0)
        Flyable.__init__ (self, Flying_speed)        

    def move (self, location):
        # print("[공중 유닛 이동]") # 출력문 제외 
        # 부모 클래스인 Flyable 의 fly() 메소드가 실행되면서 어느 방향으로 날아가는지를 출력해주기 때문
        self.fly(self.name, location)   


# 공중 공격 유닛인 레이스를 위한 rase 클래스
# 레이스는 클로킹이라는 특수 기술을 사용하면 상대방이 볼 수가 없습니다.
# 클로킹모드 여부를 확인하기 위한 cloaked 멤버변수를 정의합니다.
class rase (FlyableAttackUnit):
    def __init__ (self):
        FlyableAttackUnit.__init__ (self, "레이스", 80, 20, 6)
        self.cloaked = False    # 클로킹 모드 (해제 상태)


# 클로킹 모드를 설정하기 위한 cloaking() 메소드를 정의하는데 탱크의 시즈모드와 비슷하게
# 현재 클로킹 모드 여부에 따라서 설정 / 해제를 하도록 하며 변경된 정보를 True 또는 False로 cloaked 멤버변수에 저장합니다.
class rase (FlyableAttackUnit):
    def __init__ (self):
        FlyableAttackUnit.__init__ (self, "레이스", 80, 20, 6)
        self.cloaked = False 

    # 클로킹 모드
    def cloaking (self):
        
    # 현재 클로킹 모드일 때    
        if self.cloaking == True:
            print("{0}: 클로킹 모드를 해제합니다.". format(self.name))
            self.cloaked = False

    # 현재 클로킹 모드가 아닐 때
        else:
            print("{0}: 클로킹 모드로 설정합니다.". format(self.name))
            self.cloaked = True    


# [총정리]
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 출력문 추가

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]". format(self.name, location, self.speed))

    def damaged(self, damage): # AttackUnit 에서 Unit 으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]". format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return

        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제

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
        self.fly(self.name, location)

# 레이스
class rase (FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)

    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True