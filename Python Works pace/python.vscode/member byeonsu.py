# 멤버변수
# 클래스 내에서 정의된 변수를 멤버변수
# self. 와 함께 사용할 수 있습니다.

# 새로운 유닛을 하나 만들어보겠습니다. 
# 이번에 만들 유닛은 하늘을 날아다니는 전투기 같은 공중 유닛이고 이름은 레이스입니다.
# 멤버변수에 접근할 수 있었는데 객체를 통해 접근할 때에는 객체 이름 뒤에 점(.) 을 찍고 멤버변수 이름을 적으면 됩니다.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name    # 멤버변수 name 에 전달값 name 저장
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력: {0}, 공격력: {1}\n". format(self.hp, self.damage))
        
rase1 = Unit("레이스", 60, 90)
print("유닛 이름: {0}, 공격력: {1}". format(rase1.name, rase1.damage))  # 멤버변수 접근


# 외계인을 담당하고 있는 프로토스에는 다크 아칸이라는 마법사가 있습니다. 
# 우리편에 다크 아칸이 하나 있고 적군의 레이스를 하나 빼앗는다고 가정하겠습니다. 
# 이제 이 레이스는 우리 것이 되므로 wraith2 라는 이름으로 관리하겠습니다.
rase2 = Unit("빼앗은 레이스", 80, 100)   # 상대방 유닛을 내 것으로 만드는 것 (빼앗음)


# 그런데 레이스를 빼앗고 보니 클로킹 기능이 벌써 업그레이드가 되어 있었네요! 
# 빼앗은 레이스만을 위한 특별한 멤버 변수를 하나 정의하겠습니다.
# 이름은 .cloaking 이라고 하고 True 일 땐 클로킹 상태, False 일 땐 일반 상태라고 하죠.
rase2.cloaking = True    # 빼앗은 레이스만을 위한 특별한 멤버변수 정의
if rase2.cloaking == True:
    print("{0}는 현재 글로킹 상태입니다.". format(rase2.name))


# 우리가 직접 만든 레이스의 클로킹 여부도 확인해볼 수 있을까요? 
# 우리가 만든 레이스는 wraith1 이었으니 위와 같은 방식으로 코드를 작성 후 실행해보겠습니다.
if rase1.cloaking == True:
    print("{0}은 현재 글로킹 상태입니다.". format(rase1.name))
