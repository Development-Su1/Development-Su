# 파이썬에서는 아주 간결하게 한 줄로 된 for 반복문을 이용
# 반복 대상 항목을 하나씩 순회하면서 변수에 저장하고 그 변수를 사용자가 원하는 동작을 수행하는 방식
# [변수로 어떤 동작 for 변수 in 반복대상]


# 고등학교에서는 출석번호가 1, 2, 3, 4, 5, ... 이렇게 되어 있었는데 새학기부터는 각 번호에 100을 더한 형태
# 즉, 101, 102, 103, 104, 105, ... 이렇게 바뀐다고 합니다. 
# 우선 리스트에 5개의 출석번호 [1, 2, 3, 4, 5] 를 저장한 상태에서 한 줄 for 를 이용하여 변형을 해보겠습니다.
students = [1, 2, 3, 4, 5]
print(students)

# 한 줄 for 를 이용하여 각 항목에 100 을 더함
students = [i + 100 for i in students]  
# > 반복대상인 students 리스트에서 하나씩 값을 가져와서 i 라는 변수에 저장하고, 
# 그 변수를 활용하여 i + 100 이라는 명령을 실행한 값들을 새로운 리스트로 만들어서 students 에 집어넣는 의미
# 이 때 사용된 i 는 사용자가 임의로 사용한 이름이며, 다른 이름을 사용해도 됩니다. 
# 다만 그 이름이 "변수" 위치와 "변수로 어떤 동작" 위치에 동일하게 사용되어야 한다는 점만 주의.
# (예)
# students = [x + 100 for x in students]
# students = [name + 100 for name in students]
print(students)    # [101, 102, 103, 104, 105]


# 이름이 저장된 리스트가 있는데 한 줄 for 를 이용하여 각 이름의 길이 정보를 가지는 리스트로 변형
students = ["Iron man", "Thro", "I am groot"]
print(students)

# 한 줄 for 를 이용하여 각 이름의 길이 정보로 변환
students = [len(i) for i in students]
print(students)   # [8, 4, 10]


# 이름 정보를 가지는 동일한 리스트를 사용하되, 각 이름을 모두 대문자로 바꿔보겠습니다.
students = ["Iron man", "Thron", "I am groot"]
print(students)

# 한 줄 for 를 이용하여 각 이름을 대문자로 변경
students = [i.upper() for i in students]
print(students)

# 예제1)
students = ["lover", "stars", "josu"]
print(students)
students = [x.upper() for x in students]
print(students)

# 예제2)
students = ["LOVER", "STARS", "JOSU"]
print(students)
students = [x.lower() for x in students]
print(students)