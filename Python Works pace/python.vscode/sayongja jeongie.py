# 사용자 정의 예외처리
# 두 자리 이상의 수를 입력해서 발생한 에러라는 의미로 BigNumberError 라는 클래스를 만들고
# 파이썬에서 이미 정의되어 있는 Exception 이라는 클래스를 상속받도록 합니다. 
# 이렇게 하면 앞에서 봤던 ValueError, IndexError와 비슷하게 사용자가 필요로 하는 
# 어떤 새로운 형태의 Error 를 정의할 수 있습니다. 클래스의 내용은 일단은 pass 로 두겠습니다.
# 그리고 입력값이 10 이상인지를 확인하는 if 구문에서 ValueError 대신 새롭게 정의한 BigNumberError 를 발생시키고,
# except 구문을 추가함으로써 새로운 에러에 대한 예외 처리를 하도록 하겠습니다.
class BigNumberError(Exception):
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요.: "))
    num2 = int(input("두 번째 숫자를 입력하세요.: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError   # 사용자 정의 에러
    print("{0}/{1}={2}". format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError:    # 사용자 정의 예외 처리
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")        


# pass 부분 대신 __init__() 생성자와 __str__() 메소드를 추가합니다.
# 생성자에서는 에러 메시지를 의미하는 msg를 전달받아서 멤버변수로 설정하고, 
# __str__() 메소드에서는 멤버변수 msg를 반환해주도록 합니다. 
class BigNumbererror (Exception):
    def __init__ (self, msg):
        self.msg = msg

    def __str__ (self):
        return self.msg    


# try 구문 내에서는 BigNumberError를 발생시키는 부분의 코드를 보완하여 에러가 발생하는 시점에 
# 어떤 값들이 입력되었는지를 문자열 형태로 작성합니다. 
# 이 내용이 바로 __init__() 생성자의 msg 로 들어가게 되는 것이죠. 
# 그리고 except 구문에서는 as 를 이용하여 err 이라는 이름으로 에러를 받고 
# 이를 print() 를 통해 출력하면 __str__() 메소드에 의해 반환되는 msg 멤버변수가 출력이 됩니다.
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:   
        raise BigNumberError("입력값: {0}, {1}". format(num1, num2))   # 자세한 에러 메시지
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)    # 에러 메시지 출력


# BigNumberError의 __init__()와 __str__() 메소드는 따로 정의하지 않고 pass로만 두어도 동일하게 동작합니다. 
# 하지만 생성자에서 추가로 어떤 작업을 해야 한다거나 __str__() 메소드에서 에러 메시지를 
# 에러 코드 등과 함께 출력하고 싶은 경우에 다음과 같이 코드를 수정할 수 있습니다.
class BigNumberError (Exception):
    def __init__ (self, msg):
        self.msg = msg

    def __str__ (self):
        return "[에러코드 001]" + self.msg    # 에러 메시지 가공

# [실행결과]
# >> [에러코드 001] 입력값 : 10, 5    