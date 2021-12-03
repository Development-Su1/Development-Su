
# 앞에서 건물 유닛 클래스를 만들 때 pass 로만 남겨두었던 __init__() 생성자의 코드를 완성해보겠습니다.
# Unit 클래스를 상속받았기 때문에 Unit 의 __init__() 을 활용하면 되는데, 
# 건물은 지상 이동을 할 수 없으므로 speed 정보는 0 으로 하고 다음 줄에서 location 멤버 변수를 정의하겠습니다. 
class buildingUnit(Unit):
    def __init__ (self, name, hp ,location):
        Unit. __init__ (self, name, hp, 0)    # speed 0 : 건물은 지상 이동 불가
        self.location = location


# 클래스에서도 부모 클래스의 이름을 직접 적지 않고도 부모 클래스에 접근하는 방법이 있습니다. 
# 바로 super(). 라는 것인데요. 앞의 코드는 다음과 같이 함으로써 동일한 동작을 수행하게 됩니다. 
# 단, super(). 를 사용할 때는 self 를 제외한다는 점을 주의해주셔야 합니다.        
class buildingUnit(Unit):
    def __init__ (self, name, hp, location):
        super(). __init__ (name, hp, 0)    # 부모 클래스 접근. self 없이 사용
        self.location = location


# 하지만 부모 클래스를 2개 이상 상속하는 다중상속의 경우에는 어떻게 될까요?
# 설명을 돕기 위해 새로운 파이썬 파일을 하나 만들어서 다음과 같이 코드를 적어보겠습니다.
class Unit:
    def __init__ (self):
        print("Unit 생성자")

class Flyable:
    def __init__ (self):
        print("Flyable 생성자") 

class FlyableUnit(Unit, Flyable):
    def __init__ (self):
        super(). __init__()

dropship = FlyableUnit()                              
# [실행결과]  >> Unit 생성자


# 부모 클래스의 상속 순서를 Unit, Flyable 에서 Flyable, Unit 으로 바꿔보겠습니다.
class FlyableUnit(Flyable, Unit):
    def __init__ (self):
        super(). __init__()
# [실행결과] >> Flyable 생성자        


# 즉, 다중 상속을 받은 클래스에서 super() 를 통해 부모 클래스로 접근을 할 때는
# 순서상 가장 먼저 상속받은 클래스로 접근을 하게 됩니다. 
# 그러므로 다중 상속을 할 때 모든 부모 클래스의 생성자를 호출하려면 각 부모 클래스의 이름을 통해서 접근해야 합니다.
class FlyableUnit(Flyable, Unit):
    def __init__ (self):
        Unit. __init__ (self)    # Unit 클래스 생성자 호출
        Flyable. __init__ (self)    # Flyable 클래스 생성자 호출
# [실행결과]
# Unit 생성자
# Flyable 생성자


# [총정리]
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 순서 변경
    def __init__(self):
        # super().__init__()
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출

# 드랍쉽
dropship = FlyableUnit()