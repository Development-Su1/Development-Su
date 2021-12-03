# 가변인자(그대로 변할 수 있는 인자)

# 유재석씨는 프로그래밍 언어를 무려 5개나 공부했고, 김태호씨는 2개를 공부했습니다.
# 전달값은 lang1 ~ lang5 라고 정의
# 2개의 출력내용을 한 줄에 연달아서 출력하기 위해 첫 번째 print() 의 끝에 ,end=" " 를 적어주겠습니다.
# print() 를 실행하면 기본적으로 문장 출력 후에 줄바꿈을 하기 때문에 이후에 나오는 문장들은 새로운 줄에 표시되는데,
# end 값을 변경하면 변경된 값을 문장의 마지막으로 사용하게 됩니다.
# 그래서 줄바꿈이 아닌 띄어쓰기로, 즉 " " 로 문장을 끝내고 이후에 있는 print() 의 내용도 같은 줄에 이어서 출력할 수 있음.
def profile (name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end = " ")   # 문장 출력 후 줄바꿈 대신 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)

# 유재석씨는 5개의 언어에 대해 각각 명시를 해주면 되는데, 
# 김태호씨는 2개 언어에 대해서는 적었지만 나머지 부분은  빈 값으로 채웠습니다.
profile ("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 22, "Kotlin", "Swift", "", "", "")

# 유재석씨가 너무 재밌다고 프로그래밍 언어를 또 하나 공부하게 되면 어떨까요? 
# 이미 5개 언어를 가득 채웠는데 또 하나를 추가하게 되면, 이제는 함수 자체를 변경해야 하는 것이죠.
# 이 때 사용할 수 있는 것이 바로 가변 인자입니다.
# def 함수이름(전달값1, 전달값2, ..., *가변인자):  >>  # 가변 인자는 앞에 * 표시를 하나 추가해주면 됩니다.
#     실행 명령문1
#     실행 명령문2
#     ....
#     return 반환값

def profile (name, age, *language):   # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능  
    print("이름 : {0}\t나이 : {1}" .format(name, age), end = " ")

# print(type(language)) # tuple
# 그렇기 때문에 for 반복문을 사용하면 가변 인자로 전달받은 값들을 하나씩 반복하면서 사용할 수 있답니다.
    for lang in language:
        print(lang, end = " ")   # 언어들을 모두 한 줄에 표시
print()  # 줄바꿈 목적        

# 이제는 가변 인자 덕분에 유재석씨는 JavaScript 를 포함한 총 6개의 프로그래밍 언어 정보를 전달할 수 있게 되었고, 
# 김태호씨는 2개의 언어만 전달하면서도 뒤에 불필요한 빈 값을 적지 않아도 되겠네요.
print("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
print("김태호", 23, "Kotlin", "Swift")

# [총 정리]
def profile(name, age, *language):
    print("이름 : {0}\t나이 :{1}" .format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()    # 줄 바꿈을 하기 위해서 프린트문을 넣어둔것.
print("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
print("김태호", 23, "Kotlin", "Swift")    

# [실행 결과]
# 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript
# 이름 : 김태호   나이 : 25        Kotlin Swift







# [줄 바꿈]
# print()
# print("1")
# print("3")

# print("4")
# print("5")
# print()   # 줄 바꿈
# print("2")
# print("3")
# print("4")
# [실행 결과]
# 1
# 3
# 4
# 5

# 2
# 3
# 4
