# random 모듈의 shuffle(), sample()
# 셔플인 shuffle() 함수는 단어 뜻 그대로 섞어주는 역할을 하는 함수
# 이 함수를 이용하면 리스트 안의 데이터들을 무작위로 섞어준다.
# shuffle() 함수 사용 후에는 사용 전과 비교하여 데이터 순서가 달라질 수 있다는 점 주의

# sample() 은 리스트 내에서 원하는 갯수의 값을 뽑는 동작을 수행
# sample() 함수를 이용하면 번거로움 없이 한 번에 원하는 갯수만큼의 번호를 중복 없이 뽑을 수가 있답니다.

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)  # 원본 리스트
shuffle(lst)  # 리스트 뒤섞기
print(lst)  # 섞은 후 리스트
print(sample(lst, 1))  # 리스트 내에서 1개를 무작위로 뽑기