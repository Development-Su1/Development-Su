# try 구문을 사용할 때 finally 라는 게 있습니다. 
# finally는 try구문 내에서 에러가 발생하건 말건 try를 벗어나는 시점에 무조건 실행되는 구문입니다.
# try:
    # 실행 명령문1
    # 실행 명령문2

# except 에러 종류1:
    # 예외 처리 명령문1
    # 예외 처리 명령문2

# except 에러 종류2:
    # 예외 처리 명령문1
    # 예외 처리 명령문2

# finally:
    # 실행 명령문1
    # 실행 명령문2


# 계산기를 이용해준 모든 분들께 감사하다는 인사 메시지를 출력하도록 합니다.
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

finally:     # 에러 발생 여부 상관 없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")