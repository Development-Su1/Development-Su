# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
# 예) 생성된 비밀번호 : nav51!
# 이렇게 해서 홈페이지 url 마다 서로 다른 비밀번호를 자동으로 만들어서, 더욱 안전하게 비밀번호를 관리할 수 있게 해주는 프로그램을 개발하였습니다.

# http://naver.com 일 때
# → nav51!
# 먼저 변수를 url이라고 적음.
# 임시로 my_str 이라고 함.
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)

my_str = my_str[:my_str.index(".")] # my_str[0:5] >> 0 ~ 5 직전까지 즉, (0, 1, 2, 3, 4)까지 찍힘. 규칙2
print(my_str)

# 변수를 password로 새로 만듦
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙3
print("{0}의 비밀번호는 {1}입니다." .format(url, password))


#  http://daum.net 일 때
# → dau40!
url = "http://daum.net"
my_str = url.replace("http://", "") # 규칙1
print(my_str)

my_str = my_str[:my_str.index(".")] # my_str[0:4] >> 0 ~ 4 직전까지 즉, (0, 1, 2, 3)까지 찍힘. 규칙2
print(my_str)

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙3
print("{0}의 비밀번호는 {1}입니다." .format(url, password))


# http://google.com 일 때
# → goo61!
url = "http://google.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)

my_str = my_str[:my_str.index(".")] # my_str[0:6] >> 0 ~ 5 직전까지 즉, (0, 1, 2, 3, 4, 5)까지 찍힘. 규칙2
print(my_str)

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))


# http://youtube.com 일 때
# → you71!
url = "http://youtube.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)

my_str = my_str[:my_str.index(".")] # 규칙2
print(my_str)

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙3
print("{0}의 비밀번호는 {1}입니다." .format(url, password))

# 학교 사이트 비번 만들기
url = "http://dankook.com"
my_str = url.replace("http://", "")
print(my_str)

my_str = my_str[:my_str.index(".")]
print(my_str)

password = my_str[0:7] + str(len("my_str")) + str(my_str.count("o")) + "@"
print("{0}의 비밀번호는 {1}입니다." .format(url, password))
