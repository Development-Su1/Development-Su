# 예외처리
# 예상치 못한 어떤 실책이나 실수 또는 잘못된 무언가를 에러(error) 라고 하며 에러 상황을 처리하는 것을 예외(exception)처리라고 합니다. 
# [예외처리문] 
#  try:
#      실행 명령문1
#      실행 명령문2
#      ...
#   except 에러 종류1:
#       예외 처리 명령문1
#       예외 처리 명령문2
#       ...
#   except 에러 종류2:
#      예외 처리 명령문1
#      예외 처리 명령문2
#      ... 

# 좀 더 쉽게 이해하기 위해 사용자로부터 두 개의 수를 입력받아 나누기를 해주는 아주 간단한 계산기 프로그램을 만들어보겠습니다. 
# 아주 간단한 계산기 프로그램
print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요:"))
num2 = int(input("두 번째 숫자를 입력하세요:"))
print("{0}/{1}={2}". format(num1, num2, int(num1/num2)))

# 그런데 만약 숫자가 아닌 문자를 입력하면 어떨까요? 
# 예로 6과 "삼"을 입력해보면?? 당연히 아래의 실행결과와 같이 에러가 발생합니다.
# [실행결과]
# Traceback (most recent call last):
#   File "파일경로", line 3, in <module>
    # num2 = int(input("두 번째 숫자를 입력하세요 : "))
# ValueError: invalid literal for int() with base 10: '삼' >> 에러 발생 이유는 int( )로 감싸서 정수형으로 변환해야 하는데 "삼"은 정수로 변환을 할 수가 없는 문자이기 때문입니다.
# 에러인 ValueError:와 함께 오류 메세지가 출력됩니다.
# [위 에러를 예외처리한 코드]
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
# try 와 except 사이에서 실행되는 명령문 중에서 ValueError 가 발생하는 경우, except ValueError: 부분의 코드가 실행되고 나서 프로그램은 계속하여 실행됩니다. 
# 그러나 만약 아무 에러가 발생하지 않는다면 except 부분은 실행이 되지 않고 그냥 바로 다음 코드로 넘어가게 됩니다.    


# 프로그램을 다시 한 번 실행시키고 6 과 0 을 적어보면 에러가 발생합니다. 즉, 새로운 에러가 다시 발생한 것입니다.
# [실행결과]
# Traceback (most recent call last):
#   File "파일경로", line 5, in <module>
    # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# ZeroDivisionError: division by zero   >> 에러가 발생한 이유는 모든 수는 0 으로 나눌 수 없는데 두 번째 값으로 0 을 넣었기 때문입니다.
# >> 새로운 에러인 ZeroDivisionError 가 나오면서 메시지가 출력됩니다. 
# 이렇게 서로 다른 종류의 에러에 대해 각각 처리하려면 except 구문을 추가하여 이어서 작성하면 됩니다. 
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:    # 에러 뒤에 as 구문을 이용하여 err 라는 이름을 통해 에러 메시지를 직접 출력
    print(err)


# 새로운 코드로 예외처리 해보기
# 리스트를 사용해서 해보겠습니다.
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))     # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러!!! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)


# 위 코드에서 만약 계산 결과를 리스트에 추가하는 부분을 깜빡했다면 어떨까요? 
# IndexError와 함께 에러 메시지가 출력이 됩니다. 
# 그 이유는 현재 리스트에는 두 개의 수만 들어있으므로 index 기준으로는 [0], [1] 만 접근 가능한데 [2] 에 접근하려고 하니까 사용 가능한 리스트의 범위를 벗어났기 때문입니다.
# 여기서 예외처리를 하는데 2가지 방법이 있습니다.

# [방법 1]
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))     # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러!!! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except IndexError as err:
    print("에러!!! 사용 가능한 리스트의 범위를 벗어났습니다.")
    print(err)

# [방법 2]
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))     # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러!!! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:   # 지금까지 정의되지 않은 모든 에러에 대한 처리가 가능 (모든 에러 처리를 다 해줄 수 없는 경우)
    print("알 수 없는 에러가 발생했습니다.")
    print(err)
