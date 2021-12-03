# 에러 발생시키기
# >> [raise 에러종류]

# 계산기의 종류를 조금 바꿔서 한 자리 숫자에 대해서만 나누기를 할 수 있도록 해보겠습니다. 
# 다만 나눗셈을 하기 전에 사용자로부터 입력받은 값들이 한 자리 숫자가 맞는지 확인하여 
# 조건에 맞지 않을 때는, 즉 10 이상일 때는 의도적으로 ValueError를 발생시키고 except를 통해 예외처리를 하겠습니다.
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력해주세요.: "))
    num2 = int(input("두 번째 숫자를 입력해주세요.: "))
    if num1 >= 10 or num2 >= 10:    # 입력받은 수가 한 자리인지 확인
        raise ValueError
        print("{0}/{1}={2}". format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

    
