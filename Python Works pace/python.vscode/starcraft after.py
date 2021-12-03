# 스타그래프트 후반전
# 게임의 시작과 종료를 알리는 함수를 각각 정의하고 시작하겠습니다. 
# 스타크래프트에서는 게임을 하다가 도저히 상대방을 이길 수 없다고 판단되면 
# 졌다는 의미로 채팅창에 gg(good game) 를 입력하고 퇴장하는 것이 예의입니다.
from _typeshed import StrPath


def game_start ():
    print("[알림] 게임을 시작합니다.")

def game_over():
    print("player : gg")
    print("[player]님이 게임에서 퇴장하셨습니다.")


# 게임을 시작함과 동시에 마린 3기와 탱크 2기, 그리고 레이스 1기를 만들어보겠습니다. 
# 객체 이름은 편의상 각 유닛의 이름 첫 글자와 숫자로 정의하겠습니다.    
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = tank1()
t2 = tank2()

r1 = rase()


# 어딘가로 이동을 하거나 공격을 할 때 한꺼번에 처리하도록 하기 위해 이들을 리스트로 관리 하겠습니다.
# attack_units 라는 이름으로 리스트를 만들고 각 유닛들을 추가합니다.
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(r1)


# 1시 방향으로 모든 유닛을 이동하겠습니다. 
# 모든 유닛들은 Unit 클래스를 상속받았으므로 Unit 클래스의 move() 메소드를 사용할 수 있으며, 
# 모든 유닛들을 리스트로 관리하고 있기 때문에 반복문을 이용하여 수월하게 이동이 가능합니다.
for unit in attack_units:
    unit.move("1시")


tank.siege_developed = True
print("[알림] 탱크 시즈니 모드 개발이 완료되었습니다.")


# 마린은 스팀팩, 탱크는 시즈모드, 레이스는 클로킹모드를 각각 사용해야 합니다. 
# 리스트로 관리되는 유닛들은 서로 다른 기술을 사용해야 하는데 이들을 구분하기 위해서 isinstance()를 활용할 수 있습니다.
# isinstance(객체, 클래스)
for unit in attack_units:
    if isinstance(unit ,Marine):
        unit.stimpack()
    elif isinstance(unit, tank):
        unit.set_siege_mode()
    elif isinstance(unit, rase):
        unit.cloaking()


# 준비가 완료되었습니다. 전군 공격 명령을 통해 1시 방향으로 공격을 시도하겠습니다.
# 부모 클래스인 AttackUnit 의 attack() 메소드를 활용합니다.    
for unit in attack_units:
    unit.attack("1시")


# 전쟁을 하는 과정에서 우리 유닛들도 피해를 입습니다. 
# Unit 클래스의 damaged() 메소드를 호출하는데 피해 데미지는 랜덤으로 5 에서 20 사이의 값으로 지정하겠습니다. 
from random import*
for unit in attack_units:
    unit.damaged(randint(5, 20))


# 아쉽지만 패배를 인정하고 gg 를 선언 후 게임에서 나가도록 하겠습니다. 게임종료가 되는 것이죠.
game_over()