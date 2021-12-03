# 파일 입출력
# 파일을 열기 위해서는 open() 이라는 함수를 이용하면 되며 생김새는 이렇습니다.
# open("파일명", "열기 모드", encoding="인코딩")
# 열기 모드에는 읽기, 쓰기, 이어쓰기 등이 들어간다.
# 읽기 모드(.read, "r")
# 쓰기 모드(.write, "w")는 그 파일을 덮어쓰게 되므로 기존 내용은 다 삭제가 되며, 
# 이어쓰기 모드(.append, "a")는 그 파일의 내용 맨 밑에 이어서 쓴다는 차이점이 있습니다. 
# encoding 은 파일 내용으로 쓰는 언어와 관련된 것인데 일반적으로 "utf8" 로 설정을 해주면 
# 한글을 포함한 내용을 다룰 때에도 문제가 없습니다. 

# 학교 성적 정보를 포함하는 텍스트 파일을 만들어 보겠습니다. 
# 처음으로 파일을 만드는 것이니 쓰기 모드로 파일을 열도록 하겠습니다.
score_file = open("score.txt", "w", encoding="utf8")   # score.txt 파일을 쓰기("w") 모드로 열기
print("수학 : 0", file=score_file)   # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file)
score_file.close()   # score.txt 파일 닫기
# print() 문 내에서 file=score_file 로 함으로써 터미널이 아닌 파일에 직접 출력을 하게 된 것입니다. 
# 실행 후에 비주얼 스튜디오 코드에 보면 소스 파일과 동일한 위치에 score.txt 란 파일이 생김. 
# 파일을 열어보면 다음 내용을 포함하고 있습니다.
# 수학 : 0
# 영어 : 50
# 코드 마지막 줄에 close() 함수를 호출하는데요. 파일을 열고 나면 반드시 닫아주어야 합니다.


# 앞에서 만든 파일에 내용을 추가해보겠습니다. 
# 쓰기 모드로 열게 되면 파일을 덮어쓰게 된다고 했으므로 이어쓰기 모드로 열고, 
# print() 가 아닌 다른 방법으로 성적 정보를 추가합니다.
score_file = open("score.txt", "w", encoding="utf8")  
print("수학 : 0", file=score_file)  
print("영어 : 50", file=score_file)
score_file.close()
score_file = open("score.txt", "a", encoding = "utf8")    # score.txt 파일을 쓰기("a") 모드로 열기
score_file.write("과학 : 80")    # write() 함수를 통해서 내용을 추가
score_file.write("\n코딩 : 90")   # write는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close()

# 여기서 \n으로 줄바꿈을 하지 않으면 출력이 아래와 같이 됨.
# 수학 : 0
# 영어 : 50
# 과학 : 80코딩 : 90

# 줄바꿈을 해주면 아래와 같이 됨.
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 90


# 이 파일의 내용을 직접 읽어와서 터미널에 출력
socre_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())    # 파일 전체 읽어오기
score_file.close()


# 파일은 한 번에 모두 읽어올 수도 있지만 한 줄 한 줄 끊어서 읽어올 수도 있습니다.
# .readline() 함수를 이용하면 한 줄 단위로 불러오는데요. 
# score.txt 파일에는 현재 4줄에 걸쳐 내용이 있으므로 동일한 문장을 총 4번 반복하여 작성합니다.
# 각 문장마다 ,end="" 를 통해 줄바꿈을 하지 않도록 처리했는데요. 
# 현재 파일에 쓰여진 각 문장은 끝에 줄바꿈을 포함하고 있기에 print() 자체의 줄바꿈과 중복으로 실행되는 증상을 막기 위함임.
score_file = open("score.txt", "r", encoding = "uft8")
print(score_file.readline(), end = "")     # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")     
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")


# 대부분의 경우 파일이 총 몇 줄로 구성되었는지는 열어보기 전까지는 알 수 없습니다.
# 이 때는 while 반복문을 사용하여 읽으려는 줄이 있는 동안 계속 반복하여 읽어들이도록 할 수 있습니다.
# 더 이상 읽으려는 줄이 없을 때 반복문을 탈출하도록 하는 것인데요.
# 매 단계마다 line 이라는 변수에 한 줄씩 읽어와서 내용이 있는지 확인하고 있으면 출력, 
# 더 이상 읽어올 내용이 없으면 반복문이 탈출하게 되는 원리
score_file = open("score.txt", "r", enconding = "utf8")

while True:
    line = score_file.readline()
    if not line:     # 더 이상 읽어올 내용이 없으면?
       break     # 반복문 탈출
    print(line, end = "")     # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리

score_file.close()


# 파일 내용을 한 번에 불러와서 리스트에 저장해두고 리스트를 반복 순회하면서 내용을 출력할 수도 있습니다. 
# 이 때는 앞에서 사용한 readline() 대신 끝에 s 를 붙여서 파일 내 모든 줄을 읽어오는 readlines() 함수를 이용하여 
# lines 라는 리스트에 저장하고, while 대신 for 문을 이용하여 보다 수월하게 리스트 데이터를 순차적으로 읽어오도록 작성합니다.
score_file = open("score.txt" , "r", encoding = "utf8")

lines = score_file.readlines()    # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end = "")

score_file.close()    
