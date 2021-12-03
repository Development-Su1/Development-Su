# Quize) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

# [방법1]
from random import *
# users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 이렇게 적을 필요 없음.
# 파이썬에서는 range() 라는 걸 이용할 수가 있음. 
# 시작 값과 끝 값을 정해주면, 시작 값부터 끝 값 직전까지의 연속된 숫자를 반환해줌.
users = range(1, 21)
users = list(users)  # range 를 list 로 변환, why? >> shuffle() 은 리스트에 대해서만 사용이 가능하기 때문에
shuffle(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))  # 0 번째 인덱스 (1명)
print("커피 당첨자 : {0}" .format(winners[1:]))  # 1 번째부터 마지막까지 슬라이싱 (3명)
print("-- 축하합니다 --")
# {0}과 같이 인덱스 값을 의미하는 숫자를 넣게 되면 {0} 위치에는 뒤에 쓴 값이 들어감.


# [방법2]
# "20명 중에서 1명을 먼저 뽑고, 이 사람을 제외한 19명 중에서 3명을 뽑아야겠다. 그런데 제외를 어떻게 하지?"
from random import *
users = list(range(1,21))  # range 를 list 로 바로 감싸면 한 줄 더 줄일 수 있음.
shuffle(users)

chicken_winner = sample(users, 1)   # 치킨 당첨자 1명 추첨
remain_users = set(users) - set(chicken_winner)  # 전체 집합에서 치킨 당첨자 집합을 제외
coffee_winners = sample(remain_users, 3)  # 남은 19명 중에서 3명 추첨
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(chicken_winner))  # 이미 뽑혔으니 그대로 출력
print("커피 당첨자 : {0}" .format(coffee_winners))  # 이미 뽑혔으니 그대로 출력
print("-- 축하합니다 --")




# Quize) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 3명은 아이패드, 6명은 시계를 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 100명이 작성하였고 아이디는 1~100이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

# [방법1]
from random import *
users = list(range(1,100))
shuffle(users)
winner = sample(users, 9)
print(" -- 당첨자 발표 --")
print("아이패드 당첨자 : {0}" .format(winner[:3]))
print("시계 당첨자 : {0}" .format(winner[3:]))
print("-- 축하합니다 --")

# [방법2]
from random import *
users = list(range(1, 100))
shuffle(users)

ipad_winners = sample(users, 3)
remain_users = set(users) - set(ipad_winners)
Watch_winners = sample(remain_users, 6)

print("-- 당첨자 발표 --")
print("아이패드 당첨자 : {0}" .format(ipad_winners))  # 이미 뽑혔으니 그대로 출력
print("시계 당첨자 : {0}" .format(Watch_winners))  # 이미 뽑혔으니 그대로 출력
print("-- 축하합니다 --")