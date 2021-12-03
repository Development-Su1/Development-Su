# with 를 이용하면 파일을 열고 나서 close() 를 호출하지 않아도 자동으로 닫아주는 역할을 해줍니다.
# with 작업 as 변수명:
    # 실행 명령문1
    # 실행 명령문2
    # ...
# with 뒤에 따라오는 작업이 바로 파일을 여는 opee() 함수가 들어가는 부분입니다. 

# load() 함수를 통해서 이 파일을 열고 내용을 출력
import pickle
with open("profile.pickle", "rb") as profile_file:
     print(pickle.load(profile_file))


# study.txt 라는 텍스트 파일을 쓰기 모드인 "w" 로 열고 encoding 은 "utf8" 로 지정합니다. 
# 이렇게 만든 파일은 study_file 이라는 이름의 변수명으로 지정하고, 
# 다음 줄에서 파일에 내용을 쓰는 write() 함수를 통해서 내용을 작성합니다. (with와 함께)
with open("study.txt", "w", encoding = "utf8") as study_file:
     study_file.write("파이썬을 열심히 공부하고 있어요.")


# with 와 함께 파일을 쓸 때와 같은 이름인 study_file 로 지정하고, read() 함수를 통해서 모든 내용을 불러와서 출력합니다.
with open("study.txt", "r", encoding="utf8") as study_file:
     print(study_file.read())

# 실행해보면 앞에서 write() 함수를 통해 작성한 내용이 그대로 출력되는 것을 보실 수 있습니다.
# >> 파이썬을 열심히 공부하고 있어요.
