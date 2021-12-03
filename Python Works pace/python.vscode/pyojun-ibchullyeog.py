# 표준입출력
print("python", "java")  # python java
print("python" + "java")  #pythonjava

# sep는 분리 기호를 의미하는 separator 의 줄임말
print("python", "java", sep = ",")  # Python,Java >> 앞 코드에서는 띄어쓰기로 구분이 되었는데 이제는 콤마(,)로 구분됨

#  " vs " 라는 문자열로 구분, JavaScript 도 하나 추가
print("python", "java", "javascript", sep = " vs ")  # Python vs Java vs JavaScript >> VS로 구분

# 한 줄에 모두 엮어서 출력하려면 , end=" "
print("python", "java", "javascript", sep ="," , end = "?")  # Python,Java,javascript?무엇이 더 재밌을까요?
print("무엇이 더 재미있을까요?")  

# 만약 end= 를 적지 않았다면 결과는 이렇게 될 겁니다.
# Python,Java
# 무엇이 더 재밌을까요?


# [새로운 코드]
import sys   # sys 모듈을 가져와서 사용하겠다는 의미
print("python", "java", file=sys.stdout)  # 표준 출력 >> Python Java
print("python", "java", file=sys.stderr)  # 표준 에러 >> Python Java
# stdout 은 일반적인 내용을, stderr 는 에러 발생 시 관련 내용을 출력하기 위해 사용할 수 있습니다. 


# 학교에서 시험 성적을 받는 상황으로 가정
# 총 3과목에 대한 성적 정보를 각각 과목명(key)과 점수(value)로 하여 scores 에 저장하겠습니다. << 사전형태
# for 반복문을 이용하여 반복 대상을 scores.items() 로 입력하면, 
# scores 에 있는 각 성적 정보들이 과목명(key) 과 점수(value) 의 쌍으로, 
# 튜플형태로 넘어와서 subject 와 score 에 각각 저장됩니다.
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():  # key, value
    print(subject, scores)


# .ljust() 와 .rjust() 라는 것을 이용할 수 있습니다. 
# l 과 r 은 각각 왼쪽(left) 과 오른쪽(right) 을 의미하며, 함께 전달하는 숫자값 만큼 미리 공간을 확보하고 나서 
# 그 공간에 왼쪽 정렬 또는 오른쪽 정렬을 해주는 동작을 합니다. 이 때 값은 문자열 형태여야 합니다.
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject.ljust(7), str(score).rjust(4), sep = ":") 
# ljust(7)는 7이라는 숫자에 의해서 왼쪽으로 총 7칸의 공간을 확보
# rjust(4)는 오른쪽으로 4칸의 공간을 확보


#  zfill() 이란 것도 있다.
# 우리가 은행에 가면 대기 번호표를 뽑는데, 은행은 번호가 3자리로 표시되어 있고, 
# 번호 0 이 붙어서 001, 002, 003, ... 이런 식으로 적혀 있었습니다.
# 우선은 0 을 고려하지 않고 20번까지 대기번호를 출력해보겠습니다.
for num in range(1,21):
    print("대기번호 : " + str(num))

# 실제 은행의 대기 번호표와 같이 바꿔보겠습니다.
# .zfill() 은 함께 전달해주는 숫자만큼의 공간을 확보하고 그 공간을 zero 로, 즉 0 으로 채워주는(fill) 동작을 합니다.
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))


# 표준 입력
# input() 을 통해 입력받는 모든 값은 항상 문자열 형태로 저장됨.
answer = input("아무 값이나 입력하세요. : ")
print("입력하신 값은" + answer + "입니다.")

# 입력값 확인
answer = input("아무 값이나 입력하세요. : ")
print(type(answer))   # str, 즉 문자열 타입