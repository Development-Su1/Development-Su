# 기본값
# 굳이 무엇이다 라고 말하지 않아도 당연히 그것이겠거니 하는 내용

# 어떤 사람에 대한 기본 프로필 정보를 간략하게 출력하는 함수
def profile(name, age, main_lang):
    print("이름 :{0} \t나이 : {1}\t주 사용 언어 : {2}" .format(name, age, main_lang))
profile("유재석", 22, "파이썬")   # 유재석씨(22세)의 주 사용 언어는 파이썬
profile("김태호", 24, "자바")     # 김태호씨(24세)의 주 사용 언어는 자바


# 두 분의 나이가 같고 현재 같은 고등학교를 다니고 있으며 같은 컴퓨터 수업을 듣고 있다면 어떨까요?
# 모두 17세이며 프로그래밍 언어는 함께 수업을 듣는 파이썬 하나만 다룰 줄 안다면요? 
# 그러면 전달값 3개 중에서 나이와 주 사용 언어는 생략할 수 있지 않을까요?
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" .format(name, age, main_lang))
profile("유재석")
profile("김태호")

# [다른 방법]
def profile(main_lang, name="유재석", age=23):
    print("주 사용 언어 : {0}\t이름 : {1}\t나이 : {2}" .format(main_lang, name, age))
profile("파이썬, 자바")    