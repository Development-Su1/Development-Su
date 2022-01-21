# 문자열 처리함수
# .lower() = 소문자로 변환
# .upper() = 대문자로 변환
# .isupper() = 대문자인지 확인
# .islower() = 소문자인지 확인
# .replace( , ) = 문자열 바꾸기
# .index() = 찾으려는 문자열의 인덱스 (없으면 에러)
# .find() = 찾으려는 문자열의 인덱스 (없으면 -1)
# .count() = 문자열이 나온 횟수

python = "Python is Amazing"

print(python. lower())
print(python. upper())
print(python[0]. isupper())
print(python[1]. islower())

# 밑에서 len은 length(길이)를 말함, 파이썬은 변수임.
print(len(python))
print(python.replace("Python", "java")) # pyton을 Java로 바뀜

index = python.index("n")
print(index) # 파이썬이라는 변수에서 n이라는 글자가 몇번째 위치해 있는지 알려준다.

index = python.index("n" , index + 1) # 6번째에서 계산해서 n이 나오는 위치를 찾아준다. +1을 했기 때문에
print(index)

print(python.find("n"))
print(python.find("Java")) # 없기 때문에 -1이 나옴
# print(python.index("Java")) >> 파이썬이라는 변수에는 자바가 없기 때문에 에러를 내버림

print(python.count("n"))