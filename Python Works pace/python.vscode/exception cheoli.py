# 예외처리
# 예상치 못한 어떤 실책이나 실수 또는 잘못된 무언가를 에러(error) 라고 하며
# 에러 상황을 처리하는 것을 예외(exception) 처리라고 합니다. 

# 아주 간단한 계산기 프로그램
print("나누기 전용 계산기입니다.")
num1 = int(input("첫 번째 숫자를 입력하세요:"))
num2 = int(input("두 번째 숫자를 입력하세요:"))
print("{0}/{1}={2}". format(num1, num2, int(num1/num2)))


# 그런데 만약 숫자가 아닌 문자를 입력하면 어떨까요? 
# 프로그램을 다시 한 번 실행시키고 이번에는 6 과 "삼" 을 입력해보겠습니다.
# [실행결과]
# Traceback (most recent call last):
#   File "파일경로", line 3, in <module>
    # num2 = int(input("두 번째 숫자를 입력하세요 : "))
# ValueError: invalid literal for int() with base 10: '삼'
# >> int( )로 감싸서 정수형으로 변환해야 하는데 "삼"은 정수로 변환을 할 수가 없는 문자라서 발생하는 에러입니다.

# 에러에 대한 예외 처리는 다음과 같은 형태로 작성합니다.
# try:
    # 실행 명령문1
    # 실행 명령문2

# except 에러 종류1:
    # 예외 처리 명령문1
    # 예외 처리 명령문2

# except 에러 종류2:
    # 예외 처리 명령문1
    # 예외 처리 명령문2

# try 와 except 사이에서 실행되는 명령문 중에서 ValueError 가 발생하는 경우
# except ValueError: 부분의 코드가 실행되고 나서 프로그램은 계속하여 실행됩니다. 
# 만약 아무 에러가 발생하지 않는다면 except 부분은 실행이 되지 않고 넘어가게 되지요.
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")


# 프로그램을 다시 한 번 실행시키고 6 과 0 을 적어보겠습니다.
# [실행결과]
# Traceback (most recent call last):
#   File "파일경로", line 5, in <module>
    # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# ZeroDivisionError: division by zero
# >> 새로운 에러인 ZeroDivisionError 가 나오면서 메시지가 출력됩니다. 
# 모든 수는 0 으로 나눌 수 없는데 두 번째 값으로 0 을 넣어서 발생하는 오류이지요.
# 이렇게 서로 다른 종류의 에러에 대해 각각 처리하려면 except 구문을 추가하여 작성하면 됩니다. 
# 앞의 코드에 추가하여 ZeroDivisionError 에 대한 예외처리를 추가하는데 
# 이번에는 에러 뒤에 as 구문을 이용하여 err 이라는 이름을 통해 에러 메시지를 직접 출력해보겠습니다. 
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err)


# 이번에는 코드를 많이 바꿔보겠습니다. 
# 두 개의 수를 입력받는건 동일한데 입력받은 수를 nums라는 리스트에 추가를 하고 
# 이어서 계산 결과까지 리스트에 추가한 뒤에 print() 를 통해서 리스트의 값 3개를 순서대로 출력하겠습니다.
try:
   print("나누기 전용 계산기입니다.")
   nums = []
   nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
   nums.append(int(input("두 번째 숫자를 입력하세요: ")))
   nums.append(int(nums[0] / nums[1]))    # 계산 결과를 리스트에 추가
   print("{0}/{1}={2}". format(nums[0], nums[1], nums[0]/nums[1]))

except ValueError:
    print("오류! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err)


# 그런데 만약에 계산 결과를 리스트에 추가하는 부분을 깜빡했다면 어떨까요? 
try:
   print("나누기 전용 계산기입니다.")
   nums = []
   nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
   nums.append(int(input("두 번째 숫자를 입력하세요: ")))
#  nums.append(int(nums[0] / nums[1]))    # 계산 결과를 리스트에 추가
   print("{0}/{1}={2}". format(nums[0], nums[1], nums[0]/nums[1]))

except ValueError:
    print("오류! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err)

# [실행결과]
# 실행 후에 동일하게 6 과 3 을 입력해보니 이번에는 또 새로운 에러가 발생합니다.
# Traceback (most recent call last):
#   File "파일경로", line 38, in <module>
    # print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# IndexError: list index out of range    
# >> IndexError 와 함께 에러 메시지가 출력되는데 그 이유는 현재 리스트에는 두 개의 수만 들어있으므로
# index 기준으로는 [0], [1] 만 접근 가능한데 [2]에 접근하려고 하니 사용 가능한 리스트의 범위를 벗어나 발생한 에러입니다.
# 이번에도 IndexError 구문을 추가할 수도 있겠지만 이런 식으로 모든 에러에 대한 처리를 다 해주기는 어려움. 
# 이 때는 코드 마지막에 except Exception as err: 구문을 추가함으로써 지금까지 정의되지 않은 모든 에러에 대한 처리가능.
try:
   print("나누기 전용 계산기입니다.")
   nums = []
   nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
   nums.append(int(input("두 번째 숫자를 입력하세요: ")))
#  nums.append(int(nums[0] / nums[1]))    # 계산 결과를 리스트에 추가
   print("{0}/{1}={2}". format(nums[0], nums[1], nums[0]/nums[1]))

except ValueError:
    print("오류! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:
    print(err)

except IndexError as err:
    print("알 수 없는 에러가 발생했습니다.")
    print(err)
