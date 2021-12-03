#변수
# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult)) 

# "컨트롤 슬러시(/)를 누르면 주석 가능" 
# "다시 누르면 주석 해제"
# "str은 정수나 boolean 뒤에 붙여야 함"
# "파일명 뒤에 .py 라는 확장자를 입력함으로써 이 파일은 파이썬 소스 파일로 인식"
# + 대신 쉼표를 사용할 수도 있습니다. str() 같은 형변환을 사용하지 않아도 된다.
