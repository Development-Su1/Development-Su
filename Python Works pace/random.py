# 랜덤 함수
# 랜덤 함수를 통해서 난수를 뽑은것임
# 정수값만 보고 싶으면 앞에 int를 붙여준다.
# Alt + 방향기 >> 줄바꿈
# shift + 방향키 >> 선택적 파란줄
# Ctrl + a >> 전체 선택 
# 파이썬에는 무작위로 어떤 수를 뽑아주는 random 모듈이 있습니다.
# randrange 주어진 범위 내 임의의 정수값 생성 ex) randrange(1,46)
# randint 주어진 범위 내 임의의 정수값 생성(처음 값과 마지막 값 모두 포함) ex) randint(1,45)

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() *10) +1) # 1 ~ 10 이하의 임의의 값 생성

"로또 값 출력"
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() *45) +1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 값 생성