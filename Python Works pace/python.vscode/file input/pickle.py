# 프로그램은 실행이 끝나버리면 모든 데이터가 사라진다고 했으므로 끝나기 전에 어딘가 저장을 해야겠지요. 
# 이 때 사용할 수 있는 것이 바로 pickle 입니다. 
# pickle 은 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하거나 불러올 수 있게 해주는 모듈입니다.
# pickle 을 이용하여 데이터를 파일로 저장을 할 때는 .dump() 라는 함수를 사용하는데요.
# 첫 번째 전달값으로는 저장할 데이터를, 두 번째 전달값으로는 데이터를 저장할 파일을 적어줍니다.
# .dump(data, dest_file)

# 어떤 사람의 프로필 데이터를 만들고 저장하는 예제
# 파일 이름은 "profile.pickle" 로 하고 쓰기 모드인 "w" 로 하는데, 
# pickle 을 이용해서 저장되는 파일은 텍스트(text)가 아닌 바이너리(binary) 형태입니다. 
# 일반적인 한글, 영어, 숫자 등의 내용을 담고 있는게 텍스트 파일이라면 
# .jpg, .png 와 같은 이미지나 .mp3 와 같은 음악, 또는 .exe 와 같은 실행 파일 등이 바이너리 파일이지요.
# pickle 로 저장하는 파일 또한 바이너리 파일이기 때문에 open() 함수를 이용할 때 
# "w" 뒤에 "b" 를 붙여서 "wb" 라고 해야 올바르게 저장이 됩니다. 
# 또한 데이터 내에 한글이 포함되어 있다 하더라도 별도의 encoding 은 지정할 필요가 없습니다.
import pickle     # pickle 모듈 가져다 쓰기
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "농구"]}
print(profile)

pickle.dump(profile, profile_file)    # profile 데이터를 file 에 저장
profile_file.close()


# 데이터가 정말 잘 저장되었는지 확인하기 위해 앞에서 만든 파일을 다시 불러올텐데요. 
# 이 때는 load() 함수를 이용하고 전달값으로는 파일을 작성
# .load(src_file)
import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)    # file 에 있는 정보를 불러와서 profile 에 저장
print(profile)
profile_file.close()

# [실행결과]
{'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
