# 리스트 []
# 지하철로 예를 들어보겠습니다.
# 지하철의 각 칸마다 사람들이 몇 명씩 타고 있는지를 변수를 이용해서 나타내려면 이렇게 할 수 있습니다.
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 20

# 지금은 3칸밖에 없는데 만약 지하철이 수십 칸이라면 변수도 수십 개가 될 수 있음.
# 이 때 우리는 리스트를 이용해서 딱 하나의 이름으로 정의된 지하철을 만들 수가 있습니다.
subway = [10, 20, 30]
print(subway)

# 숫자 말고 문자열도 동일한 방법으로 사용할 수 있어요.
# 무한도전 멤버분들이 지하철 각 칸에 한 명씩 타고 있다고 해볼까요?
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 이 때 조세호씨가 몇 번째 칸에 있는지 확인하려면 문자열 처리에서 배웠던 것과 같이 index() 함수를 이용하면 됩니다.
print(subway.index("조세호")) 

# 다음 역에서 하하 씨가 지하철에 탄다고 하면, 리스트에서는 append() 함수를 쓸 수 있음.
# append() 는 리스트의 맨 마지막에 데이터를 추가하는 역할을 함.
subway.append("하하")
print(subway)

# 정형돈씨를 유재석씨와 조세호씨 사이에 끼워볼까요? 
# 인덱스 값을 이용해서 중간에 삽입도 가능해요. 
# 참고로 인덱스를 0으로 하면 리스트 맨 앞에, 즉 유재석씨 앞에 삽입이 됩니다.
subway.insert(1,"정형돈") # 1을 했기 때문에 유재석 ,조세호 사이에서 나옴.
print(subway)

subway.insert(0, "황광희")
print(subway)

# 역에 도착할 때마다 한명씩 지하철에서 내린다고 하겠습니다. 
# 리스트에서는 pop() 을 이용해서 맨 뒤에 있는 데이터를 하나씩 뺄 수 있어요. 
print(subway.pop()) # 하하가 내림
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 즉 리스트 내에 같은 값이 몇 번 사용되었는지도 볼 수 있음.
# 문자열 때와 동일하게 count() 를 쓰면 됨.
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # 설명을 위해 유재석씨를 맨 뒤에 태운 것.
print(subway)
print(subway.count("유재석"))

# 숫자로 된 리스트
num_list = [5, 2, 4, 3, 1]

# 1부터 5사이의 숫자들이 뒤섞여 있을 때 sort() 함수를 이용하면 오름차순으로 정렬을 할 수 있음.
num_list.sort()
print(num_list)

# 정렬된 리스트의 순서를 reverse() 를 이용하여 거꾸로 뒤집을 수도 있음.
num_list.reverse()
print(num_list)

# 데이터가 더 이상 필요 없다 그러면 clear() 를 통해 리스트 내의 데이터를 모두 지울 수도 있음.
num_list.clear()
print(num_list)

# 정수형, 실수형, 문자열, boolean 형, 심지어 리스트도 집어 넣을 수 있음.
mix_list = [22, "조현수", True]
print(mix_list)

# 서로 다른 리스트들을 확장할 수도 있음. >> .extend()
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 확장
print(num_list)
