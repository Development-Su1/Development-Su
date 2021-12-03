# 전달값, 반환값
# 함수 이름 옆의 괄호() 에는 필요한 갯수 만큼의 전달값이 들어가며, 
# 함수 내에서는 이 전달값들을 활용한 어떤 명령을 수행하고 나서 맨 아래에 있는 return 을 통해서 값을 반환함.
# def 함수이름(전달값1, 전달값2, ...):
#     실행 명령문1
#     실행 명령문2
#     ....
#     return 반환값1, 반환값2, ...

# 은행 계좌를 만들었으니 이번에는 처음으로 입금을 한 번 해보겠습니다. 
# deposit 이라는 함수를 만들고 2개의 값을 전달해볼텐데 
# 첫 번째 값은 현재 잔액을 의미하는 balance, 두 번째 값은 입금하려는 금액을 의미하는 money 라고 이름을 적겠습니다. 
# 함수 동작으로는 입금 완료를 안내하는 문구와 함께 현재 잔액 정보를 출력하고 잔액 정보를 return 을 통해 반환해줍니다. 
def deposit(balance, money):   # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance + money))
    return balance + money   # 입금 후 잔액 정보 반환
balance = 0   # 최초 잔액
balance = deposit(balance, 1000)  # 1000원 입금
print(balance)   # 현재 잔액    


# 출금하는 함수 
# 출금하려는 금액이 현재 계좌의 잔액보다 같거나 많아야만 가능할테니 if 조건을 통해서 금액 비교를 해야함.
def withdraw(balance, money):   # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance - money))
        return balance - money   # 출금 후 잔액 반환
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다." .format(balance))
        return balance     # 기존 잔액 반환
balance = 0
balance = deposit(balance, 1000)   

# 출금 시도
balance = withdraw(balance, 2000)   # 2000원 출금 시도 시 잔액이 부족하므로 실패
balance = withdraw(balance, 500)    # 500원 출금 시도 시 성공
print(balance)


# 저녁에 출금을 한다고 가정
# 은행 업무 시간이 아닌 경우에는 수수료를 지불해야 하는데 수수료는 100원
# 출금 후 잔액 뿐 아니라 수수료도 얼마였는지 확인할 수 있도록 둘을 함께 반환해주는 것으로 코드를 작성
def withdraw_night(balance, money):
    commission = 100   # 출금 수수료 100원
    return commission, balance - money - commission   # 튜플 형식으로 반환
balance = 0
balance = deposit(balance, 1000)

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다." .format(commission, balance))