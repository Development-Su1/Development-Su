import requests
url = "http://Hensuocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("Hensucoding.html", "w", encoding="utf8") as f:
    f.write(res.text)

#  "User-Agent"를 해줌으로써 크롬과 같이 동일한 결과를 낼 수 있다.

# 구글에 User Agent String을 쓰면 What is my Agent?가 나오는데 그 사이트를 클릭한다.
# 그러면 사이트 맨 위쪽에 어떠한 값이 나오는데 그것을 복사하여 headers라는 변수에 붙여넣기를 하면된다.
