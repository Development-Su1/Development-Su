# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.

# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
        # 출력 메세지 : "잘못된 값을 입력하였습니다."

# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        # 치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        # 출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

chicken = 10   # 남은 치킨 수
waiting = 1    # 홀 안에는 현재 만석. 대기번호 1부터 시작

while (True):
    print("[남은 치킨은: {0}]". format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken:    # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")

    else:
        print("[대기번호: {0}] {1}마리 주문이 완료되었습니다.". format(waiting, order))
        waiting += 1    # 대기번호 증가
        chicken -= order    # 주문 수 만큼 남은 치킨 감소


# 조건1에서 1보다 작거나 숫자가 아닌 입력값에 대한 예외처리를 해야 하므로 
# 소스코드를 try ~ except 구문으로 감싸주겠습니다. 
# 이 때 while구문을 통째로 감싸게 되면 잘못된 값이 입력된 경우 while구문 밖에 있는 except에서 처리가 되어서
# 프로그램이 바로 종료되기 때문에 잘못된 값이 입력되더라도 계속하여 반복문이 실행되도록 하기 위해서는 
# while구문 내부의 코드만 try ~ except 로 감싸도록 합니다.
chicken = 10
waiting = 1

while (True):
    try:
        print("[남은 치킨: {0}]". format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")

        else:
            print("[대기번호: {0}] {1}마리 주문이 완료되었습니다.". format(waiting, order))
            waiting += 1
            chicken -= order

    except VauleError:
        print("잘못된 값을 입력하였습니다.")


# "1보다 작거나"에 해당하는 조건은 아직 처리되지 않았으므로 코드를 보완하겠습니다.
chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")    

        elif order <= 0:    # 입력값이 1보다 작은 수일 때
            raise ValueError

        else:
            print("[대기번호: {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    
    except ValueError:
        print("잘못된 값을 입력하였습니다.")


# 조건 2 
# 우선 코드 맨 위에 SoldOutError 를 정의합니다. 세부 동작은 구현하지 않고 pass 로만 두겠습니다.
class SoldOutError (Exception):    # 사용자 정의 에러 (재고 소진)
    pass


# while구문 내에서 남은 치킨 수가 0이 되면 SoldOutError를 발생시키면 되겠네요. 
# 기존 if구문 아래쪽에 새로운 if를 추가하도록 합니다. 
# 그리고 이 때 발생시킨 SoldOutError를 처리하기 위해서 except SoldOutError: 구문을 추가하고 
# 조건 2 에 제시된 안내 문구를 출력하도록 합니다. 
# 그리고 이 상황에서는 더 이상 주문을 받을 수 없기 때문에 break를 통해서 while구문을 탈출하여 프로그램이 종료.
chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")    
        
        elif order <= 0:
            raise ValueError    
        
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except VauleError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break


# [총정리]
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        
        if order > chicken:
            print("재료가 부족합니다.")    
        
        elif order <= 0:
            raise ValueError    
        
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break