# 지역변수, 전역변수
# 지역 변수란 함수 내에서만 쓸 수 있는 변수이며, 전역 변수는 모든 곳에서 쓸 수 있는 변수입니다.

# 어느 부대의 총기함에 총이 10자루가 있고 2명이 경계근무를 나가는 과정에서 남은 총을 구하는 예제
gun = 10

def checkpoint(soliders):   # 경계근무 나가는 군인 수
    gun = 20
    gun = gun - soliders    # 전체 총에서 경계근무 나가는 군인 수만큼 뺀 잔여 총
    print("[함수 내] 남은 총 : {0}" .format(gun))

print("전체 총 : {0}" .format(gun))
checkpoint(2)   # 2명이 경계 근무 출발
print("남은 총 : {0}" .format(gun))  

# [실행결과]
# 전체 총 : 10
# [함수 내] 남은 총 : 18 
# 남은 총 : 10


# 전체 총과 남은 총은 10 으로 변함이 없고 checkpoint() 함수 내에서 새롭게 선언된 gun 에는 20 이라는 값이 저장되었다가 
# 군인 수만큼 2를 빼니 18 로 줄어들었네요. 하지만 실제로 총기함에는 2자루의 총이 줄어든 8자루라고 나와야 정상이겠죠?
# 해결책은 바로 전역변수(global) 이라는 키워드입니다. 함수 내에서 전역변수를 사용하겠다는 의미인데요. 
# global gun 이라고만 하면 전역 공간에 선언된 변수를 그대로 사용하며 그 값을 직접 변경할 수도 있습니다.
gun = 10

def checkpoint(soliders):
    global gun   # 전역공간에 있는 gun 이라는 변수를 사용
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}" .format(gun))

print("전체 총 : {0}" .format(gun))
checkpoint(2)
print("남은 총 : {0}" .format(gun))    

# [실행결과]
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8


# 앞에서 작성한 코드를 전역변수가 없는 버전으로 만들어 보겠습니다. 전달값과 반환값을 적절히 활용하는 방법이며, 
# 반환(return) 을 의미하는 내용을 담아 checkpoint_ret() 라는 새로운 함수로 정의하겠습니다.
gun = 10

def checkpoint_ret(gun, soldiers):   # 전체 총 수와 군인 수를 전달받음
    gun = gun - soldiers    # 전달받은 gun 을 사용
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
gun= checkpoint_ret(gun, 2)    # gun 값을 함수에 전달
print("남은 총 : {0}" .format(gun))