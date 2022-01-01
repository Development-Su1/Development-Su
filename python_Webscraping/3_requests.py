import requests
res = requests.get("http://google.com")
#res = requests.get("http://Hensucoding.tistory.com")
res.raise_for_status()
#print("응답코드 :", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)



import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print("웹 스크래핑을 시작합니다.")
# 위 코드는 웹 스크래핑을 하기 위해서 올바른 코드를 가져왔다 그러면 문제가 없고 그렇지 않은 경우에는 에러를 내버림.

#print("응답코드 :", res.status_code) # 200 이면 정상 
# if res.status_code == requests.codes.ok: >> [requests.codes.ok가 200이랑 똑같은 것임.]
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)    
